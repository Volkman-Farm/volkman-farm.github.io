#!/usr/bin/env node
// Publish to Instagram via the Instagram API with Instagram Login.
// https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/
//
// Usage:
//   node scripts/ig-publish.mjs whoami
//   node scripts/ig-publish.mjs image <public-jpeg-url> [--location <id>] <caption...>
//   node scripts/ig-publish.mjs carousel <url1,url2,...> [--location <id>] <caption...>
//   node scripts/ig-publish.mjs story <public-jpeg-url>          (no location support)
//   node scripts/ig-publish.mjs refresh
//
// --location takes a Facebook place-page ID (known IDs live in INSTAGRAM-PLAN.md).
// Stories cannot carry a location; Meta's API does not support it there.
//
// Env, from .env at the repo root or the environment:
//   IG_USER_ID        Instagram professional account ID (whoami prints it)
//   IG_ACCESS_TOKEN   long-lived Instagram Login token (60-day; refresh prints a new one)
//   IG_API_VERSION    optional, defaults below
//
// Constraints that live on Meta's side: JPEG only, media must be publicly
// reachable at publish time, 100 API posts per rolling 24 hours.

import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const envFile = join(root, '.env');
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^([A-Z_]+)=(.*)$/);
    if (m && !process.env[m[1]]) process.env[m[1]] = m[2].trim();
  }
}

const TOKEN = process.env.IG_ACCESS_TOKEN;
const USER_ID = process.env.IG_USER_ID;
const VERSION = process.env.IG_API_VERSION || 'v23.0';
const BASE = `https://graph.instagram.com/${VERSION}`;

function die(msg) {
  console.error(msg);
  process.exit(1);
}

async function api(path, params = {}, method = 'GET') {
  const url = new URL(path.startsWith('https://') ? path : `${BASE}${path}`);
  const body = new URLSearchParams({ access_token: TOKEN, ...params });
  const res = method === 'GET'
    ? await fetch(`${url}?${body}`)
    : await fetch(url, { method, body });
  const json = await res.json();
  if (!res.ok || json.error) {
    die(`API error on ${url.pathname}:\n${JSON.stringify(json.error ?? json, null, 2)}`);
  }
  return json;
}

// Media containers process asynchronously; wait until publishable.
async function waitForContainer(id) {
  for (let i = 0; i < 30; i++) {
    const { status_code } = await api(`/${id}`, { fields: 'status_code' });
    if (status_code === 'FINISHED') return;
    if (status_code === 'ERROR') die(`Container ${id} failed processing.`);
    await new Promise((r) => setTimeout(r, 2000));
  }
  die(`Container ${id} not ready after 60s; not publishing.`);
}

async function publish(containerId) {
  await waitForContainer(containerId);
  const { id } = await api(`/${USER_ID}/media_publish`, { creation_id: containerId }, 'POST');
  const { permalink } = await api(`/${id}`, { fields: 'permalink' });
  console.log(`Published: ${permalink ?? id}`);
}

const [, , cmd, ...rest] = process.argv;
if (!cmd) die('Usage: ig-publish.mjs <whoami|image|carousel|story|refresh> ...');
if (!TOKEN) die('IG_ACCESS_TOKEN is not set. Copy .env.example to .env and fill it in.');

// Pull "--location <id>" out of the args, wherever it appears.
let locationId;
const locIdx = rest.indexOf('--location');
if (locIdx !== -1) {
  [, locationId] = rest.splice(locIdx, 2);
  if (!locationId) die('--location needs a place ID.');
}
const withLocation = (params) => (locationId ? { ...params, location_id: locationId } : params);

switch (cmd) {
  case 'whoami': {
    const me = await api('/me', { fields: 'user_id,username,account_type' });
    console.log(JSON.stringify(me, null, 2));
    break;
  }

  case 'refresh': {
    const json = await api('https://graph.instagram.com/refresh_access_token', {
      grant_type: 'ig_refresh_token',
    });
    console.log(`New token (expires in ${Math.round(json.expires_in / 86400)} days), update .env:`);
    console.log(json.access_token);
    break;
  }

  case 'image': {
    const [url, ...caption] = rest;
    if (!url || !USER_ID) die('Usage: ig-publish.mjs image <public-jpeg-url> <caption> (IG_USER_ID must be set)');
    const { id } = await api(`/${USER_ID}/media`, withLocation({ image_url: url, caption: caption.join(' ') }), 'POST');
    await publish(id);
    break;
  }

  case 'carousel': {
    const [urls, ...caption] = rest;
    const list = (urls ?? '').split(',').filter(Boolean);
    if (list.length < 2 || !USER_ID) die('Usage: ig-publish.mjs carousel <url1,url2,...> <caption> (2-10 urls)');
    const children = [];
    for (const image_url of list) {
      const { id } = await api(`/${USER_ID}/media`, { image_url, is_carousel_item: 'true' }, 'POST');
      await waitForContainer(id);
      children.push(id);
    }
    const { id } = await api(`/${USER_ID}/media`, withLocation({
      media_type: 'CAROUSEL',
      children: children.join(','),
      caption: caption.join(' '),
    }), 'POST');
    await publish(id);
    break;
  }

  case 'story': {
    const [url] = rest;
    if (!url || !USER_ID) die('Usage: ig-publish.mjs story <public-jpeg-url>');
    const { id } = await api(`/${USER_ID}/media`, { media_type: 'STORIES', image_url: url }, 'POST');
    await publish(id);
    break;
  }

  default:
    die(`Unknown command: ${cmd}`);
}
