from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path("assets")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
W, H = 1200, 800


def font(size):
    return ImageFont.truetype(FONT, size)


def text(d, xy, s, size, fill, anchor=None):
    f = font(size)
    d.text(xy, s, font=f, fill=fill, anchor=anchor)


def shadow_card(img, box, banner):
    x, y, w, h = box
    banner = banner.resize((w - 20, h - 20), Image.LANCZOS)
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x+8, y+10, x+w+8, y+h+10), radius=18, fill=(0, 0, 0, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB"))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x+w, y+h), radius=18, fill=(255, 255, 255, 255), outline=(210, 215, 220), width=2)
    img.paste(banner, (x+10, y+10))


def make_hero(banner_path, out, bg, accent, lines):
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    for i in range(-400, W + 400, 80):
        d.line((i, H, i + 360, 0), fill=tuple(min(255, c + 8) for c in bg), width=2)

    y = 170
    for s, size, color in lines:
        text(d, (70, y), s, size, color)
        y += size + 34

    shadow_card(img, (620, 190, 550, 430), Image.open(banner_path).convert("RGB"))
    img.save(OUT / out, "JPEG", quality=88, optimize=True)


def make_thumb(banner_path, out, label, color):
    im = Image.open(banner_path).convert("RGB")
    im = im.resize((600, 500), Image.LANCZOS)
    canvas = Image.new("RGB", (600, 600), (255, 250, 242))
    canvas.paste(im, (0, 0))
    d = ImageDraw.Draw(canvas)
    d.rectangle((0, 500, 600, 600), fill=color)
    f = font(34)
    box = d.textbbox((0, 0), label, font=f)
    d.text(((600 - (box[2]-box[0])) / 2, 525), label, font=f, fill=(255, 255, 255))
    canvas.save(OUT / out, "JPEG", quality=88, optimize=True)


make_hero(
    "assets/gmo-banner.jpg", "hikari-hero.jpg", (240, 246, 252), (60, 92, 130),
    [("光回線の乗り換え", 58, (45, 70, 100)),
     ("GMOとくとくBB", 48, (190, 40, 40)),
     ("× ドコモ光", 46, (60, 92, 130)),
     ("工事費・キャッシュバックを比較", 26, (110, 120, 130))],
)
make_thumb("assets/gmo-banner.jpg", "hikari-thumb.jpg", "GMO × ドコモ光", (60, 92, 130))

make_hero(
    "assets/jani-banner.jpg", "goods-hero.jpg", (255, 250, 232), (150, 110, 20),
    [("グッズ買取の比較", 58, (90, 60, 20)),
     ("Jani King", 52, (180, 130, 20)),
     ("ジャニーズグッズ買取専門", 30, (110, 80, 30)),
     ("無料査定から始めよう", 26, (140, 110, 60))],
)
make_thumb("assets/jani-banner.jpg", "goods-thumb.jpg", "Jani King 買取", (160, 120, 20))

for n in ["hikari-hero.jpg", "hikari-thumb.jpg", "goods-hero.jpg", "goods-thumb.jpg"]:
    print(n, (OUT / n).stat().st_size)
