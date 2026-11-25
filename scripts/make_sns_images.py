from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("sns/assets")
OUT.mkdir(exist_ok=True)
FONT_B = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
FONT_R = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"

W = H = 1080
CREAM = (255, 247, 236)
RED = (178, 58, 46)
DARK = (120, 36, 30)
GOLD = (201, 162, 39)
INK = (44, 36, 30)


def font(size, bold=False):
    f = ImageFont.truetype(FONT_B if bold else FONT_R, size)
    return f


def center_text(d, y, text, size, fill, bold=False, spacing=8):
    f = font(size, bold)
    box = d.textbbox((0, 0), text, font=f)
    w = box[2] - box[0]
    d.text(((W - w) / 2, y), text, font=f, fill=fill, spacing=spacing)
    return y + (box[3] - box[1]) + spacing


def draw_jubako(d, cx, cy, scale=1.0):
    s = scale
    d.rounded_rectangle((cx - 230*s, cy - 170*s, cx + 230*s, cy - 108*s), radius=14*s, fill=DARK)
    d.ellipse((cx - 22*s, cy - 192*s, cx + 22*s, cy - 160*s), fill=DARK)
    tiers = [
        (cy - 95*s, cy - 25*s, RED),
        (cy - 15*s, cy + 55*s, GOLD),
        (cy + 65*s, cy + 135*s, RED),
    ]
    for y1, y2, color in tiers:
        d.rounded_rectangle((cx - 215*s, y1, cx + 215*s, y2), radius=10*s, fill=color)
        for x in range(-150, 180, 90):
            d.ellipse((cx + x*s, (y1+y2)/2 - 13*s, cx + (x+26)*s, (y1+y2)/2 + 13*s), fill=CREAM)
    d.rounded_rectangle((cx - 235*s, cy + 145*s, cx + 235*s, cy + 170*s), radius=8*s, fill=DARK)


def base():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 18), fill=RED)
    d.rectangle((0, H-18, W, H), fill=RED)
    return img, d


# おせち早割
img, d = base()
d.text((48, 46), "年末ごちそうガイド", font=font(34, True), fill=RED)
y = center_text(d, 120, "おせち 早割", 92, INK, True)
y = center_text(d, y + 10, "12/10まで", 132, RED, True)
draw_jubako(d, W//2, 660, 1.15)
y = center_text(d, 880, "料亭おせち 4,800円〜", 54, DARK, True)
center_text(d, y + 8, "早割のうちに確保しよう", 40, INK)
img.save(OUT / "osechi-post-1080.png")

# かに 内容量
img, d = base()
d.text((48, 46), "年末ごちそうガイド", font=font(34, True), fill=RED)
y = center_text(d, 120, "かに 内容量の目安", 76, INK, True)
y = center_text(d, y + 16, "1人 500〜700g", 100, RED, True)
# crab-ish simple legs decoration
for i in range(6):
    x = 250 + i*110
    d.arc((x-70, 440, x+70, 580), 200, 340, fill=GOLD, width=18)
    d.arc((x-70, 500, x+70, 640), 20, 160, fill=RED, width=18)
center_text(d, 700, "2人で鍋＋焼き：1.5〜2.0kg", 52, DARK, True)
center_text(d, 790, "3〜4人で囲む：2.5〜3.5kg", 52, DARK, True)
center_text(d, 910, "見た目ではなく「内容量」で選ぶ", 42, INK)
img.save(OUT / "kani-post-1080.png")

for f in ["osechi-post-1080.png", "kani-post-1080.png"]:
    p = OUT / f
    print(f, p.stat().st_size, Image.open(p).size)
