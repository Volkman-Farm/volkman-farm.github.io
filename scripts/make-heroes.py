#!/usr/bin/env python3
"""Generate the Sep 11-21 hero SVGs in the volkman.farm house style."""
import os, math

BG="#f5ead3"; BR="#5c4633"; GR="#3a5a2a"; OL="#8a7e3a"; DK="#1f2419"; RD="#6b2a2f"
OUT="/Users/albertvolkman/Sites/volkman.farm/assets/blog"

def svg(alt, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" role="img" '
            f'aria-label="{alt}">\n  <rect width="1200" height="630" fill="{BG}"/>\n{body}</svg>\n')

def g(body, stroke=BR, w=8, fill="none", extra=""):
    return (f'  <g fill="{fill}" stroke="{stroke}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"{extra}>\n{body}  </g>\n\n')

def sprout(bx, by, s=1.0, lean=0.0):
    """Stem with two leaf lobes. Origin at stem base. Matches the seed-sourcing glyph."""
    t=lambda dx,dy:(bx+dx*s+lean*dy*-0.06, by+dy*s)
    p=[]
    x0,y0=t(0,-44); p.append(f'    <path d="M{bx} {by} L {x0:.0f} {y0:.0f}"/>\n')
    a=t(0,-38); b=t(-22,-40); c=t(-34,-52); d=t(-34,-68); e=t(-14,-68); f=t(-1,-56)
    p.append(f'    <path d="M{a[0]:.0f} {a[1]:.0f} C {b[0]:.0f} {b[1]:.0f} {c[0]:.0f} {c[1]:.0f} {d[0]:.0f} {d[1]:.0f} '
             f'C {e[0]:.0f} {e[1]:.0f} {f[0]:.0f} {f[1]:.0f} {a[0]:.0f} {a[1]:.0f} Z"/>\n')
    a=t(0,-30); b=t(22,-32); c=t(34,-44); d=t(34,-60); e=t(14,-60); f=t(1,-48)
    p.append(f'    <path d="M{a[0]:.0f} {a[1]:.0f} C {b[0]:.0f} {b[1]:.0f} {c[0]:.0f} {c[1]:.0f} {d[0]:.0f} {d[1]:.0f} '
             f'C {e[0]:.0f} {e[1]:.0f} {f[0]:.0f} {f[1]:.0f} {a[0]:.0f} {a[1]:.0f} Z"/>\n')
    return "".join(p)

def leafmark(x, y, s=1.0, flip=False):
    """Small scattered leaf, for greens showing through a lid or strewn on food."""
    d=-1 if flip else 1
    return (f'    <path d="M{x} {y} C {x-4*s*d:.0f} {y-8*s:.0f} {x+4*s*d:.0f} {y-11*s:.0f} '
            f'{x+10*s*d:.0f} {y-8*s:.0f}"/>\n')

def clamshell(x, y, w, h, seam=None):
    seam = seam if seam is not None else h*0.42
    return (f'    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5"/>\n'
            f'    <path d="M{x} {y+seam:.0f} H {x+w}"/>\n')

def ground(y, x1=120, x2=1080, stroke=BR, w=8):
    return g(f'    <path d="M{x1} {y} H {x2}"/>\n', stroke, w)

FILES={}

# ---------------------------------------------------------------- Sep 11 water
def leaf(x, y, ang, L=40, W=13):
    ux,uy=math.cos(math.radians(ang)),math.sin(math.radians(ang))
    p=lambda a,w:(x+ux*L*a-uy*w, y+uy*L*a+ux*w)
    c1,c2,tip,c3,c4=p(.3,W),p(.75,W),p(1,0),p(.75,-W),p(.3,-W)
    return (f'    <path d="M{x:.0f} {y:.0f} C {c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {tip[0]:.0f} {tip[1]:.0f} '
            f'C {c3[0]:.0f} {c3[1]:.0f} {c4[0]:.0f} {c4[1]:.0f} {x:.0f} {y:.0f} Z"/>\n')
def drop(x, y):
    return (f'    <path d="M{x} {y-18} C {x+4} {y-8} {x+11} {y} {x+11} {y+8} '
            f'C {x+11} {y+15} {x+6} {y+20} {x} {y+20} C {x-6} {y+20} {x-11} {y+15} {x-11} {y+8} '
            f'C {x-11} {y} {x-4} {y-8} {x} {y-18} Z"/>\n')
b =ground(400, 80, 1120)
b+=g('    <path d="M330 400 C 334 450 324 510 330 584"/>\n', BR, 7)
b+=g('    <path d="M331 418 C 296 426 258 446 222 486"/>\n'
     '    <path d="M331 418 C 366 428 404 448 440 490"/>\n'
     '    <path d="M328 468 C 298 480 272 506 256 552"/>\n'
     '    <path d="M332 468 C 362 482 390 508 404 554"/>\n'
     '    <path d="M329 528 C 312 544 302 564 298 590"/>\n'
     '    <path d="M331 528 C 348 546 358 566 362 592"/>\n', BR, 6)
b+=g('    <path d="M278 440 C 272 460 266 474 264 494"/>\n'
     '    <path d="M384 440 C 392 460 398 476 402 496"/>\n'
     '    <path d="M286 500 C 270 506 250 512 232 520"/>\n'
     '    <path d="M376 500 C 394 506 414 514 430 522"/>\n', BR, 4)
tom ='    <path d="M330 400 C 324 330 338 250 330 160"/>\n'
tom+='    <path d="M331 336 C 358 326 386 318 414 318"/>\n'
tom+='    <path d="M328 276 C 302 266 276 262 250 264"/>\n'
tom+='    <path d="M331 212 C 352 200 372 188 388 170"/>\n'
for x,y,angs in ((414,318,(-45,-5,35)),(250,264,(145,185,225)),(388,170,(-95,-50,-5)),
                 (330,160,(-125,-90,-55)),(372,322,(-80,70)),(290,266,(-100,100)),(360,196,(-120,20))):
    tom+="".join(leaf(x,y,a) for a in angs)
tom+='    <path d="M280 266 L 282 290"/>\n    <path d="M392 320 L 394 340"/>\n'
tom+='    <path d="M274 292 Q 284 286 294 292"/>\n    <path d="M386 342 Q 396 336 406 342"/>\n'
b+=g(tom, GR, 6)
b+=g('    <circle cx="284" cy="314" r="24"/>\n    <circle cx="396" cy="362" r="22"/>\n', RD, 7)
b+=g('    <rect x="700" y="336" width="360" height="64" rx="6"/>\n')
greens=""; mat=""
specs=[(0.78,-0.3),(0.90,0.2),(0.72,0.4),(0.86,-0.2),(0.80,0.1),
       (0.94,-0.4),(0.74,0.3),(0.88,0.0),(0.82,-0.25),(0.76,0.35)]
for i,(sc,ln) in enumerate(specs):
    x=730+i*33; d=-1 if i%2 else 1
    greens+=sprout(x, 336, sc, ln)
    mat+=f'    <path d="M{x} 342 C {x-7} 356 {x+6} 372 {x-2} 390"/>\n'
    mat+=f'    <path d="M{x-1} 364 C {x-6*d} 370 {x-12*d} 374 {x-18*d} 382"/>\n'
mat+='    <path d="M712 388 C 760 382 800 394 850 386 C 900 380 950 392 1000 386 C 1020 384 1040 388 1048 386"/>\n'
b+=g(greens, GR, 6)
b+=g(mat, BR, 3)
b+=g(drop(230,150)+drop(468,118)+drop(820,214)+drop(890,186)+drop(956,222), OL, 0, OL)
FILES['water-why-filtered-matters']=(
 "Line drawing of a tomato plant with roots spreading deep into the soil beside a shallow tray of microgreens whose roots are a thin mat, with water drops falling over both", b)

# ------------------------------------------------------- Sep 12 how much order
b =ground(520, 90, 1110)
b+=g(clamshell(240,350,320,170,72), DK, 8)
b+=g("".join(leafmark(x,410,1.5) for x in (280,340,400,460,510)), GR, 5)
b+=g(clamshell(620,410,180,110,46), DK, 7)
b+=g("".join(leafmark(x,452,1.2) for x in (650,700,750)), GR, 5)
b+=g('    <ellipse cx="918" cy="502" rx="112" ry="29"/>\n'
     '    <ellipse cx="918" cy="500" rx="84" ry="19"/>\n', BR, 7)
b+=g('    <path d="M1066 386 V 502"/>\n'
     '    <path d="M1044 386 V 422"/>\n    <path d="M1066 384 V 422"/>\n    <path d="M1088 386 V 422"/>\n'
     '    <path d="M1044 422 Q 1066 442 1088 422"/>\n', BR, 6)
FILES['how-much-should-i-order']=(
 "Line drawing of two clamshell containers of different sizes side by side on a counter, with a plate and a fork beside the smaller one", b)

# ------------------------------------------------- Sep 13 which green fits
b =ground(500, 60, 1140)
row=""
specs=[(1.05,0.0),(1.35,-0.3),(1.18,0.25),(0.92,0.0),(1.40,0.35),(1.00,-0.4),(1.22,0.15)]
for i,(sc,ln) in enumerate(specs):
    x=124+i*112
    row+=sprout(x, 500, sc, ln)
    row+=sprout(x-24, 500, sc*0.76, ln-0.35)
    row+=sprout(x+24, 500, sc*0.70, ln+0.4)
b+=g(row, GR, 6)
b+=g('    <path d="M262 418 C 284 400 290 374 274 358"/>\n', GR, 5)
b+=g("".join(f'    <circle cx="{908+i*98}" cy="454" r="34"/>\n' for i in range(3)),
     BR, 5, extra=' stroke-dasharray="15 13"')
FILES['which-green-fits-your-kitchen']=(
 "Line drawing of seven small bunches of microgreens arranged in a row on a counter, each with a different leaf shape, and three empty spots at the end of the row", b)

# ------------------------------------------------------ Sep 14 avocado toast
b =ground(500, 120, 1080)
b+=g('    <path d="M380 470 V 374 Q 380 358 398 358 L 688 358 Q 706 358 706 374 V 470 Z"/>\n'
     '    <path d="M402 470 V 380 H 684 V 470"/>\n')
b+=g('    <path d="M384 358 C 412 326 458 340 498 330 C 542 319 590 338 634 329 C 670 322 694 338 704 358"/>\n', GR, 7)
b+=g(sprout(474,330,0.84,-0.4)+sprout(524,324,1.00,0.0)+sprout(574,330,0.90,0.45)+
     sprout(500,328,0.70,0.25)+sprout(550,328,0.74,-0.25), GR, 6)
b+=g('    <rect x="822" y="466" width="104" height="28" rx="12"/>\n'
     '    <path d="M926 470 L 1082 476 L 1082 482 L 926 490 Z"/>\n', BR, 7)
FILES['avocado-toast-but-make-it-yours']=(
 "Line drawing of a thick slice of toast with mashed avocado and a small pile of microgreens on top, a knife resting beside it", b)

# ------------------------------------------------- Sep 15 two weeks paddocks
b =g('    <rect x="180" y="130" width="840" height="330" rx="6"/>\n'
     '    <rect x="232" y="182" width="736" height="226" rx="6"/>\n'
     '    <path d="M600 182 V 408"/>\n')
posts=""
for x in range(180,1021,84):
    posts+=f'    <path d="M{x} 122 V 138"/>\n    <path d="M{x} 452 V 468"/>\n'
b+=g(posts, BR, 6)
tufts=""
for i,x in enumerate(range(190,1015,36)):
    h=14+(i%3)*5
    tufts+=f'    <path d="M{x} 500 V {500-h}"/>\n    <path d="M{x-9} 500 V {500-h+5}"/>\n    <path d="M{x+9} 500 V {500-h+4}"/>\n'
b+=g(tufts, GR, 5)
b+=ground(520, 150, 1050)
FILES['two-weeks-and-nothing-has-come-back']=(
 "Line drawing of two fenced poultry paddocks side by side with a narrow corridor between the outer and inner fence lines, and short mowed grass along the base", b)

# ------------------------------------------------- Sep 16 food forest mound
b =ground(520, 80, 1120)
b+=g('    <path d="M200 520 C 300 380 460 336 600 336 C 740 336 900 380 1000 520"/>\n')
b+=g('    <path d="M600 336 V 258"/>\n'
     '    <path d="M600 124 C 648 116 690 146 692 184 C 728 196 730 240 694 254 '
     'C 672 270 634 270 600 262 C 566 270 528 268 506 252 '
     'C 470 238 472 194 508 184 C 510 146 552 116 600 124 Z"/>\n', BR, 8)
for cx,cy in ((398,384),(802,384)):
    b+=g(f'    <path d="M{cx} {cy} C {cx-32} {cy} {cx-50} {cy-22} {cx-46} {cy-44} '
         f'C {cx-42} {cy-74} {cx-18} {cy-90} {cx} {cy-88} '
         f'C {cx+18} {cy-90} {cx+42} {cy-74} {cx+46} {cy-44} '
         f'C {cx+50} {cy-22} {cx+32} {cy} {cx} {cy} Z"/>\n', GR, 7)
cover=""
for x0,x1,y0,y1 in ((330,236,398,500),(286,196,430,506),(870,964,398,500),(914,1004,430,506)):
    cover+=f'    <path d="M{x0} {y0} C {(x0+x1)//2} {y0+34} {x1} {y1-46} {x1} {y1}"/>\n'
b+=g(cover, GR, 7)
b+=g(sprout(502,352,0.5)+sprout(690,352,0.5)+sprout(600,336,0.44), GR, 5)
FILES['the-food-forest-question']=(
 "Line drawing of a planted mound in cross section with a small tree at the top, shrubs at the shoulder, and sprawling ground cover running down the sides", b)

# --------------------------------------------------- Sep 17 rain and routes
b =g('    <path d="M320 186 H 1100"/>\n    <path d="M330 208 H 1090"/>\n'
     '    <path d="M362 208 V 520"/>\n    <path d="M1074 208 V 520"/>\n'
     '    <path d="M340 520 H 1120"/>\n    <path d="M340 520 V 560"/>\n'
     '    <path d="M60 560 H 340"/>\n')
b+=g('    <rect x="872" y="250" width="176" height="270" rx="4"/>\n'
     '    <rect x="900" y="276" width="120" height="72" rx="3"/>\n'
     '    <circle cx="892" cy="404" r="9"/>\n', DK, 7)
b+=g(clamshell(452,462,120,58,26), DK, 7)
b+=g("".join(leafmark(x,488,1.1) for x in (476,510,542)), GR, 5)
rain=""
for i,x in enumerate(range(86,338,30)):
    for j in range(3):
        y=76+j*158+(i%3)*30
        rain+=f'    <path d="M{x} {y} L {x-18} {y+78}"/>\n'
b+=g(rain, BR, 5)
FILES['rain-days-and-route-days']=(
 "Line drawing of a covered porch with a clamshell of greens tucked into a dry corner beside the door, rain falling in straight lines beyond the overhang", b)

# ------------------------------------------------------ Sep 18 every tray weighed
b =ground(540, 100, 1100)
# scale: base, platform slab, display
b+=g('    <rect x="280" y="434" width="400" height="106" rx="8"/>\n'
     '    <rect x="266" y="398" width="428" height="36" rx="8"/>\n'
     '    <rect x="340" y="456" width="150" height="46" rx="5"/>\n', BR, 8)
b+=g('    <path d="M366 479 H 388"/>\n    <path d="M400 479 H 424"/>\n'
     '    <path d="M436 479 H 456"/>\n', OL, 5)
# bowl of seed sitting on the platform
b+=g('    <path d="M280 286 C 310 438 650 438 680 286"/>\n'
     '    <path d="M280 286 H 680"/>\n', BR, 8)
seeds=""
import random
random.seed(11)
for i in range(30):
    x=random.randint(322,638)
    lift=int(30*(1-abs(x-480)/175.0))
    y=random.randint(286-max(lift,8), 284)
    seeds+=f'    <circle cx="{x}" cy="{y}" r="{random.choice((5,6,6,7))}"/>\n'
b+=g(seeds, DK, 0, DK)
# the tray it is going into, still bare
b+=g('    <rect x="800" y="452" width="330" height="88" rx="6"/>\n'
     '    <path d="M800 482 H 1130"/>\n', BR, 8)
FILES['every-tray-gets-weighed']=(
 "Line drawing of a kitchen scale holding a bowl of seed, with a bare seeding tray waiting beside it", b)

# ---------------------------------------------------------- Sep 19 gift card
b =g('    <path d="M340 400 H 880"/>\n'
     '    <path d="M340 400 V 452"/>\n    <path d="M880 400 V 452"/>\n'
     '    <path d="M280 452 H 940"/>\n'
     '    <path d="M280 452 V 508"/>\n    <path d="M940 452 V 508"/>\n'
     '    <path d="M220 508 H 1000"/>\n')
b+=g('    <path d="M436 404 L 532 390 L 540 408 L 448 422 Z"/>\n'
     '    <path d="M488 397 L 496 415"/>\n', BR, 6)
b+=g(clamshell(480,302,260,98,42), DK, 8)
b+=g("".join(leafmark(x,344,1.5) for x in (516,570,624,678)), GR, 6)
FILES['can-i-gift-a-delivery']=(
 "Line drawing of a clamshell of microgreens sitting on a porch step with a small folded card tucked under its edge", b)

# ------------------------------------------------------ Sep 20 cotyledon
b =g('    <rect x="160" y="470" width="880" height="70" rx="6"/>\n'
     '    <path d="M160 494 H 1040"/>\n')
def cots(bx, top, spread=1.0, drop=0):
    a=(bx, top+6+drop)
    return (f'    <path d="M{bx} {a[1]} C {bx-30*spread:.0f} {a[1]-2} {bx-48*spread:.0f} {a[1]-16} '
            f'{bx-48*spread:.0f} {a[1]-36} C {bx-22*spread:.0f} {a[1]-38} {bx-4:.0f} {a[1]-20} {bx} {a[1]} Z"/>\n'
            f'    <path d="M{bx} {a[1]+8} C {bx+30*spread:.0f} {a[1]+6} {bx+48*spread:.0f} {a[1]-8} '
            f'{bx+48*spread:.0f} {a[1]-28} C {bx+22*spread:.0f} {a[1]-30} {bx+4:.0f} {a[1]-12} {bx} {a[1]+8} Z"/>\n')
s1=f'    <path d="M380 470 V 366"/>\n'+cots(380,366)
s2=f'    <path d="M600 470 V 356"/>\n'+cots(600,362)+ \
   '    <path d="M600 356 C 592 328 594 304 600 290 C 606 304 608 328 600 356 Z"/>\n'
s3=f'    <path d="M820 470 V 320"/>\n'+cots(820,378,1.15)+ \
   '    <path d="M820 330 C 800 320 782 300 780 272 C 802 274 818 300 820 330 Z"/>\n' \
   '    <path d="M820 342 C 840 332 858 312 860 284 C 838 286 822 312 820 342 Z"/>\n'
b+=g(s1+s2+s3, GR, 7)
FILES['cotyledon-or-true-leaf']=(
 "Line drawing of three seedlings side by side at different stages, the first with two rounded seed leaves, the second with a small pointed leaf emerging between them, the third fuller", b)

# --------------------------------------------------------- Sep 21 flatbreads
b =ground(566, 120, 1080)
b+=g('    <rect x="228" y="118" width="452" height="424" rx="40"/>\n'
     '    <path d="M680 254 L 1058 266 Q 1076 272 1076 288 L 1076 372 Q 1076 388 1058 394 L 680 406"/>\n')
b+=g('    <circle cx="452" cy="330" r="172"/>\n'
     '    <circle cx="452" cy="330" r="144"/>\n', BR, 8)
b+=g('    <path d="M452 330 L 452 158"/>\n'
     '    <path d="M452 330 L 601 244"/>\n'
     '    <path d="M452 330 L 601 416"/>\n', BR, 7)
pieces=[(372,244,2.0,False),(448,220,1.9,True),(522,262,1.8,False),
        (344,320,1.9,True),(424,346,2.0,False),(506,330,1.8,True),
        (386,412,1.9,False),(466,436,1.8,True),(548,396,1.7,False),
        (318,388,1.7,True),(560,320,1.6,False),(400,180,1.6,True),
        (486,166,1.5,False),(322,254,1.6,True),(470,388,1.7,False),
        (356,458,1.5,True)]
b+=g("".join(leafmark(x,y,s,f) for x,y,s,f in pieces), GR, 6)
FILES['flatbreads-and-pizza-night']=(
 "Line drawing of a pizza on a wooden peel with two slices cut, a handful of microgreens scattered across the top after baking", b)

for name,(alt,body) in FILES.items():
    p=os.path.join(OUT,name+".svg")
    open(p,"w").write(svg(alt,body))
    print(f"wrote {name}.svg  ({os.path.getsize(p)} bytes)")
print(f"\n{len(FILES)} files")
