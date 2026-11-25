from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

SRC = Path("sns/assets/kani-real-test.jpg")
OUT = Path("sns/assets/kani-post-1080.png")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"

im = Image.open(SRC).convert("RGB")
w, h = im.size
side = h
left = (w - side) // 2
crop = im.crop((left, 0, left + side, side)).resize((1080, 1080), Image.LANCZOS)

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)
d.rectangle((0, 0, 1080, 250), fill=(20, 16, 14, 175))
d.rectangle((0, 830, 1080, 1080), fill=(20, 16, 14, 190))


def center(text, y, size, fill):
    f = ImageFont.truetype(FONT, size)
    box = d.textbbox((0, 0), text, font=f)
    tw = box[2] - box[0]
    d.text(((1080 - tw) / 2, y), text, font=f, fill=fill)


center("かに 内容量の目安", 40, 62, (255, 255, 255))
center("1人 500〜700g", 130, 82, (255, 210, 120))
center("2人で鍋＋焼き：1.5〜2.0kg", 860, 46, (255, 255, 255))
center("3〜4人で囲む：2.5〜3.5kg", 935, 46, (255, 255, 255))
center("見た目ではなく「内容量」で選ぶ", 1020, 34, (225, 220, 210))

result = Image.alpha_composite(crop.convert("RGBA"), overlay).convert("RGB")
result.save(OUT)
print(OUT, result.size, OUT.stat().st_size)
