from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("sns/assets/profile-icon.png")
S = 500
NAVY = (22, 50, 79)
TEAL = (14, 116, 144)
WHITE = (255, 255, 255)
GOLD = (201, 162, 39)


def font(size):
    return ImageFont.truetype("C:\\Windows\\Fonts\\NotoSansJP-VF.ttf", size)


img = Image.new("RGB", (S, S), (244, 247, 250))
d = ImageDraw.Draw(img)

# rounded-square app icon with diagonal gradient
grad = Image.new("RGB", (S, S))
gd = ImageDraw.Draw(grad)
for y in range(S):
    t = y / S
    c = tuple(int(NAVY[i] * (1 - t) + TEAL[i] * t) for i in range(3))
    gd.line((0, y, S, y), fill=c)
mask = Image.new("L", (S, S), 0)
md = ImageDraw.Draw(mask)
md.rounded_rectangle((20, 20, S - 20, S - 20), radius=110, fill=255)
img.paste(grad, (0, 0), mask)

d = ImageDraw.Draw(img)

# comparison card symbol
d.rounded_rectangle((120, 120, 380, 300), radius=26, fill=WHITE)
d.rounded_rectangle((148, 152, 352, 178), radius=10, fill=(210, 226, 234))
d.rounded_rectangle((148, 196, 352, 222), radius=10, fill=(210, 226, 234))
d.rounded_rectangle((148, 240, 300, 266), radius=10, fill=(210, 226, 234))
# check mark
d.line((300, 258, 322, 280, 366, 228), fill=TEAL, width=16, joint="curve")

# gold accent dot
d.ellipse((382, 100, 418, 136), fill=GOLD)

# label
f = font(36)
t = "比較ガイド"
box = d.textbbox((0, 0), t, font=f)
d.text(((S - (box[2] - box[0])) / 2, 340), t, font=f, fill=WHITE)

img.save(OUT)
print(OUT, OUT.stat().st_size)
