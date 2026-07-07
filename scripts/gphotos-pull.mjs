#!/usr/bin/env node
// Pull photos from Google Photos via the Photos Picker API.
// https://developers.google.com/photos/picker/reference/rest/v1/sessions
//
// Google removed general library read access in March 2025; the Picker flow is
// the supported path. This script opens a picking session, hands you the
// picker link (open it on the phone, select photos), then downloads the
// originals once you finish.
//
// Usage:
//   node scripts/gphotos-pull.mjs auth            one-time OAuth consent on this Mac
//   node scripts/gphotos-pull.mjs pull [outDir]   start a session, wait, download (default: ig-inbox/)
//
// Env, from .env at the repo root or the environment:
//   GPHOTOS_CLIENT_ID / GPHOTOS_CLIENT_SECRET   Desktop-app OAuth client from Google Cloud
// Refresh token is stored in .gphotos-token.json (gitignored).

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { createServer } from 'node:http';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const envFile = join(root, '.env');
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^([A-Z_]+)=(.*)$/);
    if (m && !process.env[m[1]]) process.env[m[1]] = m[2].trim();
  }
}

const CLIENT_ID = process.env.GPHOTOS_CLIENT_ID;
const CLIENT_SECRET = process.env.GPHOTOS_CLIENT_SECRET;
const TOKEN_FILE = join(root, '.gphotos-token.json');
const SCOPE = 'https://www.googleapis.com/auth/photospicker.mediaitems.readonly';
const API = 'https://photospicker.googleapis.com/v1';

function die(msg) {
  console.error(msg);
  process.exit(1);
}

if (!CLIENT_ID || !CLIENT_SECRET) {
  die('GPHOTOS_CLIENT_ID / GPHOTOS_CLIENT_SECRET not set. See INSTAGRAM-PLAN.md, "Publishing pipeline".');
}

async function tokenRequest(params) {
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    body: new URLSearchParams({ client_id: CLIENT_ID, client_secret: CLIENT_SECRET, ...params }),
  });
  const json = await res.json();
  if (!res.ok) die(`OAuth error:\n${JSON.stringify(json, null, 2)}`);
  return json;
}

// One-time consent via loopback redirect on this Mac.
async function auth() {
  const port = 8763;
  const redirect = `http://127.0.0.1:${port}`;
  const code = await new Promise((resolve) => {
    const server = createServer((req, res) => {
      const c = new URL(req.url, redirect).searchParams.get('code');
      res.end(c ? 'Authorized. You can close this tab.' : 'Missing code.');
      if (c) { server.close(); resolve(c); }
    }).listen(port, () => {
      const url = new URL('https://accounts.google.com/o/oauth2/v2/auth');
      url.search = new URLSearchParams({
        client_id: CLIENT_ID,
        redirect_uri: redirect,
        response_type: 'code',
        scope: SCOPE,
        access_type: 'offline',
        prompt: 'consent',
      });
      console.log('Opening Google consent in your browser...');
      execFile('open', [url.toString()]);
    });
  });
  const tok = await tokenRequest({ grant_type: 'authorization_code', code, redirect_uri: redirect });
  writeFileSync(TOKEN_FILE, JSON.stringify({ refresh_token: tok.refresh_token }, null, 2));
  console.log(`Refresh token saved to ${TOKEN_FILE}. You will not need to do this again.`);
}

async function accessToken() {
  if (!existsSync(TOKEN_FILE)) die('Not authorized yet. Run: node scripts/gphotos-pull.mjs auth');
  const { refresh_token } = JSON.parse(readFileSync(TOKEN_FILE, 'utf8'));
  const tok = await tokenRequest({ grant_type: 'refresh_token', refresh_token });
  return tok.access_token;
}

async function api(token, path, method = 'GET') {
  const res = await fetch(`${API}${path}`, { method, headers: { Authorization: `Bearer ${token}` } });
  if (res.status === 204) return {};
  const json = await res.json();
  if (!res.ok) die(`Picker API error on ${path}:\n${JSON.stringify(json.error ?? json, null, 2)}`);
  return json;
}

const seconds = (dur) => parseFloat(dur ?? '3') || 3; // "3.5s" -> 3.5

async function pull(outDir) {
  const token = await accessToken();
  const session = await api(token, '/sessions', 'POST');
  console.log('\nPick your photos here (open on the phone):\n');
  console.log(`  ${session.pickerUri}\n`);

  const interval = seconds(session.pollingConfig?.pollInterval);
  const deadline = Date.now() + Math.min(seconds(session.pollingConfig?.timeoutIn) || 600, 600) * 1000;
  let done = false;
  process.stdout.write('Waiting for selection');
  while (Date.now() < deadline) {
    await new Promise((r) => setTimeout(r, interval * 1000));
    process.stdout.write('.');
    const s = await api(token, `/sessions/${session.id}`);
    if (s.mediaItemsSet) { done = true; break; }
  }
  console.log('');
  if (!done) {
    await api(token, `/sessions/${session.id}`, 'DELETE');
    die('Timed out waiting for a selection. Run pull again.');
  }

  mkdirSync(outDir, { recursive: true });
  const saved = [];
  let pageToken = '';
  do {
    const page = await api(token, `/mediaItems?sessionId=${session.id}&pageSize=100${pageToken && `&pageToken=${pageToken}`}`);
    for (const item of page.mediaItems ?? []) {
      if (item.type !== 'PHOTO') { console.log(`Skipping non-photo: ${item.mediaFile?.filename}`); continue; }
      // baseUrl requires a size/download param and the bearer header; =d keeps original pixels.
      const res = await fetch(`${item.mediaFile.baseUrl}=d`, { headers: { Authorization: `Bearer ${token}` } });
      if (!res.ok) die(`Download failed for ${item.mediaFile.filename}: HTTP ${res.status}`);
      const file = join(outDir, item.mediaFile.filename);
      writeFileSync(file, Buffer.from(await res.arrayBuffer()));
      saved.push(file);
      console.log(`Saved ${file}`);
    }
    pageToken = page.nextPageToken ?? '';
  } while (pageToken);

  await api(token, `/sessions/${session.id}`, 'DELETE');
  if (!saved.length) die('Selection was empty.');
  console.log(`\n${saved.length} photo(s) in ${outDir}`);
}

const [, , cmd, outArg] = process.argv;
if (cmd === 'auth') await auth();
else if (cmd === 'pull') await pull(outArg || join(root, 'ig-inbox'));
else die('Usage: gphotos-pull.mjs <auth|pull [outDir]>');
