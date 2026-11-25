from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("sns/assets")
OUT.mkdir(exist_ok=True)
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"

W = H = 1080
CREAM = (255, 248, 236)
RED = (178, 58, 46)
DARK = (120, 36, 30)
GOLD = (201, 162, 39)
INK = (44, 36, 30)
WHITE = (255, 255, 255)
GREEN = (74, 110, 60)
BLACK = (38, 32, 28)


def font(size):
    return ImageFont.truetype(FONT, size)


def center_text(d, y, text, size, fill):
    f = font(size)
    box = d.textbbox((0, 0), text, font=f)
    w = box[2] - box[0]
    d.text(((W - w) / 2, y), text, font=f, fill=fill)
    return y + (box[3] - box[1]) + 8


def seigaiha_bg(d):
    for row in range(0, H, 90):
        for col in range(-90, W + 90, 90):
            x = col + (45 if (row // 90) % 2 else 0)
            for r in (22, 38, 54):
                d.arc((x - r, row - r, x + r, row + r), 180, 360, fill=(245, 228, 200), width=2)


def kuromame(d, x, y):
    for dx, dy in [(0, 0), (26, -8), (52, 4), (14, 20), (42, 24)]:
        d.ellipse((x+dx, y+dy, x+dx+22, y+dy+22), fill=BLACK)
        d.ellipse((x+dx+5, y+dy+4, x+dx+11, y+dy+10), fill=(90, 80, 70))


def kamaboko(d, x, y):
    d.pieslice((x, y, x+86, y+86), 180, 360, fill=WHITE)
    d.pieslice((x+30, y, x+86, y+86), 180, 360, fill=RED)
    d.arc((x, y, x+86, y+86), 180, 360, fill=GOLD, width=3)


def daidai(d, x, y):
    d.ellipse((x, y+8, x+66, y+74), fill=(240, 160, 35))
    d.ellipse((x+8, y+16, x+30, y+38), fill=(255, 195, 80))
    d.ellipse((x+28, y-4, x+62, y+22), fill=GREEN)


def ebi(d, x, y):
    for i in range(4):
        off = i * 18
        d.arc((x+off, y, x+off+60, y+70), 250, 450, fill=(235, 120, 60), width=12)
    d.ellipse((x+48, y+34, x+78, y+62), fill=(255, 170, 100))


def kazunoko(d, x, y):
    for dx in range(0, 90, 18):
        for dy in range(0, 54, 18):
            d.ellipse((x+dx, y+dy, x+dx+14, y+dy+14), fill=(245, 210, 90), outline=(210, 165, 55), width=1)


def kombumaki(d, x, y):
    for i in range(3):
        ox = i * 34
        d.ellipse((x+ox, y, x+ox+42, y+52), fill=(52, 78, 58))
        d.arc((x+ox+8, y+8, x+ox+34, y+44), 0, 360, fill=GOLD, width=3)
        d.arc((x+ox+15, y+14, x+ox+29, y+38), 0, 360, fill=(120, 150, 100), width=2)


def kuri(d, x, y):
    for i in range(3):
        ox = i * 32
        d.ellipse((x+ox, y+10, x+ox+34, y+48), fill=(130, 78, 40))
        d.polygon([(x+ox+10, y+8), (x+ox+24, y+8), (x+ox+17, y+2)], fill=(90, 50, 25))


def anago(d, x, y):
    for i in range(3):
        ox = i * 46
        d.rounded_rectangle((x+ox, y+6, x+ox+40, y+50), radius=8, fill=(150, 90, 45))
        d.line((x+ox+6, y+18, x+ox+34, y+18), fill=(90, 50, 25), width=3)
        d.line((x+ox+6, y+34, x+ox+34, y+34), fill=(90, 50, 25), width=3)


def draw_jubako(d):
    x0, x1 = 170, 910
    y0, y1 = 330, 810
    # lid
    d.rounded_rectangle((x0-12, y0-44, x1+12, y0+6), radius=10, fill=DARK, outline=GOLD, width=4)
    d.ellipse((530, y0-62, 576, y0-30), fill=GOLD)
    # box
    d.rounded_rectangle((x0, y0, x1, y1), radius=12, fill=(110, 32, 28), outline=GOLD, width=5)
    tiers = [(y0+12, y0+154), (y0+164, y0+306), (y0+316, y0+458)]
    for i, (a, b) in enumerate(tiers):
        d.rectangle((x0+8, a, x1-8, b), fill=DARK)
        d.line((x0+8, b, x1-8, b), fill=GOLD, width=3)
    # tier 1
    kuromame(d, 200, 360)
    kamaboko(d, 380, 356)
    daidai(d, 540, 352)
    ebi(d, 680, 356)
    # tier 2
    kazunoko(d, 205, 512)
    kombumaki(d, 365, 515)
    kuri(d, 550, 516)
    daidai(d, 720, 512)
    # tier 3
    anago(d, 205, 664)
    kamaboko(d, 405, 660)
    kuromame(d, 560, 662)
    ebi(d, 720, 660)


def draw_crab(d):
    cx, cy = 540, 570
    # legs
    for side in (-1, 1):
        for i in range(4):
            y = cy - 30 + i * 38
            d.line((cx + side*90, y, cx + side*210, y + (i-1)*18), fill=RED, width=16)
            d.line((cx + side*210, y + (i-1)*18, cx + side*250, y + (i-1)*18 - 24), fill=RED, width=12)
    # claws
    for side in (-1, 1):
        bx = cx + side*200
        d.ellipse((bx-70, cy-150, bx+70, cy-40), fill=(225, 95, 60))
        d.polygon([(bx+side*10, cy-120), (bx+side*95, cy-160), (bx+side*85, cy-80)], fill=(225, 95, 60))
    # body
    d.ellipse((cx-130, cy-70, cx+130, cy+110), fill=RED)
    d.arc((cx-130, cy-70, cx+130, cy+110), 200, 340, fill=(150, 45, 35), width=6)
    # eyes
    for side in (-1, 1):
        ex = cx + side*55
        d.line((ex, cy-55, ex, cy-95), fill=RED, width=8)
        d.ellipse((ex-16, cy-115, ex+16, cy-83), fill=WHITE)
        d.ellipse((ex-6, cy-107, ex+6, cy-95), fill=BLACK)


def base():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    seigaiha_bg(d)
    d.rectangle((0, 0, W, 16), fill=RED)
    d.rectangle((0, H-16, W, H), fill=RED)
    return img, d


# おせち
img, d = base()
d.text((54, 44), "年末ごちそうガイド", font=font(34), fill=RED)
center_text(d, 105, "おせち 早割", 86, INK)
center_text(d, 208, "12/10まで", 112, RED)
draw_jubako(d)
center_text(d, 852, "料亭おせち 4,800円〜", 50, DARK)
center_text(d, 928, "早割のうちに確保しよう", 38, INK)
img.save(OUT / "osechi-post-1080.png")

# かに
img, d = base()
d.text((54, 44), "年末ごちそうガイド", font=font(34), fill=RED)
center_text(d, 105, "かに 内容量の目安", 72, INK)
center_text(d, 200, "1人 500〜700g", 96, RED)
draw_crab(d)
center_text(d, 830, "2人で鍋＋焼き：1.5〜2.0kg", 48, DARK)
center_text(d, 910, "3〜4人で囲む：2.5〜3.5kg", 48, DARK)
center_text(d, 990, "見た目ではなく「内容量」で選ぶ", 36, INK)
img.save(OUT / "kani-post-1080.png")

for f in ["osechi-post-1080.png", "kani-post-1080.png"]:
    p = OUT / f
    print(f, p.stat().st_size, Image.open(p).size)
