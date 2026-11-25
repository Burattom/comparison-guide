from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

SRC = Path("sns/assets/osechi-real-test.jpg")
OUT = Path("sns/assets/osechi-post-1080.png")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"

im = Image.open(SRC).convert("RGB")
# 1500x1000 -> center-ish square crop including the jubako
crop = im.crop((250, 0, 1250, 1000)).resize((1080, 1080), Image.LANCZOS)

overlay = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)
d.rectangle((0, 790, 1080, 1080), fill=(20, 16, 14, 185))


def center(text, y, size, fill):
    f = ImageFont.truetype(FONT, size)
    box = d.textbbox((0, 0), text, font=f)
    w = box[2] - box[0]
    d.text(((1080 - w) / 2, y), text, font=f, fill=fill)


center("おせち 早割", 820, 70, (255, 255, 255))
center("12/10まで", 910, 100, (255, 210, 120))
center("料亭おせち 4,800円〜", 1030, 38, (230, 225, 215))

result = Image.alpha_composite(crop.convert("RGBA"), overlay).convert("RGB")
result.save(OUT)
print(OUT, result.size, OUT.stat().st_size)
