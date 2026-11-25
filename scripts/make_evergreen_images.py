from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("assets")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
W, H = 1200, 800


def base(top, bottom):
    img = Image.new("RGB", (W, H), bottom)
    d = ImageDraw.Draw(img)
    for i in range(0, W, 60):
        d.line((i, 0, i - 200, H), fill=top, width=2)
    return img, d


# 光回線
img, d = base((232, 240, 248), (248, 251, 255))
d.rounded_rectangle((430, 270, 770, 560), radius=24, fill=(60, 92, 130))
d.rounded_rectangle((470, 310, 730, 520), radius=14, fill=(240, 246, 252))
for x in (510, 600, 690):
    d.ellipse((x-12, 360, x+12, 384), fill=(70, 110, 160))
d.line((600, 440, 600, 480), fill=(70, 110, 160), width=8)
for r in (90, 160, 230):
    d.arc((600-r, 300-r, 600+r, 300+r), 200, 340, fill=(90, 150, 210), width=10)
f = ImageFont.truetype(FONT, 64)
t = "光回線の乗り換え"
box = d.textbbox((0, 0), t, font=f)
d.text(((W-(box[2]-box[0]))/2, 630), t, font=f, fill=(50, 75, 105))
img.save(OUT / "hikari-hero.jpg", "JPEG", quality=82, optimize=True)
img.crop((300, 100, 900, 700)).resize((600, 600)).save(OUT / "hikari-thumb.jpg", "JPEG", quality=82, optimize=True)

# グッズ買取
img, d = base((250, 238, 244), (255, 249, 252))
for i, x in enumerate((320, 450, 580, 710)):
    d.rounded_rectangle((x, 250 + (i % 2) * 30, x + 110, 500 + (i % 2) * 30), radius=10,
                        fill=(210, 120, 150) if i % 2 == 0 else (150, 110, 170))
    d.ellipse((x+30, 330, x+80, 380), fill=(255, 245, 235))
f = ImageFont.truetype(FONT, 64)
t = "グッズ買取の比較"
box = d.textbbox((0, 0), t, font=f)
d.text(((W-(box[2]-box[0]))/2, 630), t, font=f, fill=(130, 70, 95))
img.save(OUT / "goods-hero.jpg", "JPEG", quality=82, optimize=True)
img.crop((300, 100, 900, 700)).resize((600, 600)).save(OUT / "goods-thumb.jpg", "JPEG", quality=82, optimize=True)

for n in ["hikari-hero.jpg", "hikari-thumb.jpg", "goods-hero.jpg", "goods-thumb.jpg"]:
    print(n, (OUT / n).stat().st_size)
