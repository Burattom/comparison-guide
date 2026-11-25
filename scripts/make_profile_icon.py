from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("sns/assets/profile-icon.png")
S = 500
CREAM = (255, 248, 236)
BLUE = (60, 92, 130)
GOLD = (201, 162, 39)
RED = (178, 58, 46)

img = Image.new("RGB", (S, S), CREAM)
d = ImageDraw.Draw(img)
d.ellipse((20, 20, S-20, S-20), outline=BLUE, width=16)

# wifi arcs
for r in (55, 95, 135):
    d.arc((S//2 - r, 185 - r, S//2 + r, 185 + r), 200, 340, fill=BLUE, width=12)
d.ellipse((S//2-12, 173, S//2+12, 197), fill=BLUE)

# buyback box with arrow
d.rounded_rectangle((150, 280, 350, 400), radius=12, fill=GOLD)
d.line((250, 250, 250, 340), fill=RED, width=12)
d.polygon([(225, 320), (275, 320), (250, 355)], fill=RED)

font = ImageFont.truetype("C:\\Windows\\Fonts\\NotoSansJP-VF.ttf", 30)
t = "比較ガイド"
box = d.textbbox((0, 0), t, font=font)
d.text(((S-(box[2]-box[0]))/2, 425), t, font=font, fill=RED)

img.save(OUT)
print(OUT, OUT.stat().st_size)
