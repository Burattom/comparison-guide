from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path("assets")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
W, H = 1200, 800


def font(size):
    return ImageFont.truetype(FONT, size)


# NURO: use official key visual
kv = Image.open(OUT / "official-nuro-kv.jpg").convert("RGB")
target_ratio = W / H
w, h = kv.size
if w / h > target_ratio:
    nw = int(h * target_ratio)
    kv = kv.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
kv.resize((W, H), Image.LANCZOS).save(OUT / "nuro-hero.jpg", "JPEG", quality=88, optimize=True)
# thumb: crop right side of KV (gamer) square
th = Image.open(OUT / "official-nuro-kv.jpg").convert("RGB")
tw, thh = th.size
side = min(thh, tw // 2)
th = th.crop((tw - side, (thh - side) // 2, tw, (thh + side) // 2)).resize((600, 600), Image.LANCZOS)
d = ImageDraw.Draw(th)
d.rectangle((0, 540, 600, 600), fill=(20, 50, 79))
t = "NURO光"
f = font(34)
box = d.textbbox((0, 0), t, font=f)
d.text(((600 - (box[2]-box[0])) / 2, 550), t, font=f, fill=(255, 255, 255))
th.save(OUT / "nuro-thumb.jpg", "JPEG", quality=88, optimize=True)

# au: compose official banner with text panel
img = Image.new("RGB", (W, H), (250, 246, 240))
d = ImageDraw.Draw(img)
for i in range(-300, W + 300, 90):
    d.line((i, H, i + 350, 0), fill=(245, 240, 232), width=2)
d.text((70, 90), "比較ガイド", font=font(32), fill=(190, 70, 40))
d.rounded_rectangle((70, 150, 250, 196), radius=22, fill=(190, 70, 40))
box = d.textbbox((0, 0), "独自回線", font=font(28))
d.text((160 - (box[2]-box[0])/2, 158), "独自回線", font=font(28), fill=(255, 255, 255))
d.text((70, 250), "auひかり", font=font(64), fill=(60, 50, 45))
d.text((70, 360), "実測速度・回線種別・選び方", font=font(32), fill=(120, 110, 100))
d.text((70, 430), "失敗しない乗り換えの確認ポイント", font=font(28), fill=(150, 140, 130))
d.rectangle((70, 520, 520, 526), fill=(190, 70, 40))

x, y, w2, h2 = 615, 145, 550, 550
shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((x+8, y+10, x+w2+8, y+h2+10), radius=16, fill=(0, 0, 0, 70))
shadow = shadow.filter(ImageFilter.GaussianBlur(12))
img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")
d = ImageDraw.Draw(img)
d.rounded_rectangle((x, y, x+w2, y+h2), radius=16, fill=(255, 255, 255), outline=(220, 215, 210), width=2)
b = Image.open(OUT / "official-au-bnr06.jpg").convert("RGB").resize((w2-20, h2-20), Image.LANCZOS)
img.paste(b, (x+10, y+10))
img.save(OUT / "au-hero.jpg", "JPEG", quality=88, optimize=True)

th = Image.open(OUT / "official-au-bnr06.jpg").convert("RGB").resize((600, 600), Image.LANCZOS)
th.save(OUT / "au-thumb.jpg", "JPEG", quality=88, optimize=True)

for n in ["nuro-hero.jpg", "nuro-thumb.jpg", "au-hero.jpg", "au-thumb.jpg"]:
    print(n, (OUT / n).stat().st_size)
