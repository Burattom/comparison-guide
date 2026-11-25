from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path("assets")
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
W, H = 1200, 800

PROVIDERS = {
    "docomo": ("ドコモ光", "光コラボ", (240, 246, 252), (60, 92, 130)),
    "gmo": ("GMO光アクセス", "光コラボ", (240, 248, 250), (14, 116, 144)),
    "softbank": ("SoftBank光", "光コラボ", (248, 244, 252), (120, 70, 150)),
    "softbank2": ("GMOソフトバンク光", "光コラボ", (250, 244, 248), (160, 60, 90)),
    "flets": ("フレッツ光", "NTTフレッツ", (244, 248, 252), (40, 90, 140)),
    "nuro": ("NURO光", "独自回線", (240, 246, 252), (20, 80, 120)),
    "au": ("auひかり", "独自回線", (250, 246, 240), (190, 70, 40)),
}


def font(size):
    return ImageFont.truetype(FONT, size)


def center(d, y, text, size, fill, x=W // 2):
    f = font(size)
    box = d.textbbox((0, 0), text, font=f)
    d.text((x - (box[2] - box[0]) / 2, y), text, font=f, fill=fill)


def card(img, banner_path):
    x, y, w, h = 615, 175, 555, 455
    b = Image.open(banner_path).convert("RGB")
    b.thumbnail((w - 20, h - 20), Image.LANCZOS)
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x+8, y+10, x+w+8, y+h+10), radius=16, fill=(0, 0, 0, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB"))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x+w, y+h), radius=16, fill=(255, 255, 255), outline=(215, 222, 230), width=2)
    bx = x + (w - b.width) // 2
    by = y + (h - b.height) // 2
    img.paste(b, (bx, by))


for key, (name, kind, bg, accent) in PROVIDERS.items():
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    for i in range(-300, W + 300, 90):
        d.line((i, H, i + 350, 0), fill=tuple(min(255, c + 6) for c in bg), width=2)

    d.text((70, 90), "比較ガイド", font=font(32), fill=accent)
    d.rounded_rectangle((70, 150, 250, 196), radius=22, fill=accent)
    center(d, 158, kind, 28, (255, 255, 255), 160)
    d.text((70, 250), name, font=font(64), fill=(30, 50, 70))
    d.text((70, 360), "実測速度・回線種別・選び方", font=font(32), fill=(100, 115, 130))
    d.text((70, 430), "失敗しない乗り換えの確認ポイント", font=font(28), fill=(130, 145, 160))
    d.rectangle((70, 520, 520, 526), fill=accent)

    if key in ("nuro", "au"):
        # original illustration (no logo / trademark)
        d.ellipse((700, 220, 1080, 600), outline=accent, width=8)
        for r in (110, 160, 210):
            d.arc((890 - r, 420 - r, 890 + r, 420 + r), 200, 340, fill=accent, width=10)
        d.ellipse((876, 406, 904, 434), fill=accent)
        d.text((735, 620), "独自回線", font=font(40), fill=accent)
    else:
        card(img, OUT / f"provider-{key}.jpg")

    img.save(OUT / f"{key}-hero.jpg", "JPEG", quality=88, optimize=True)

    # square thumb from hero right side / banner
    th = Image.new("RGB", (600, 600), bg)
    if key in ("nuro", "au"):
        td = ImageDraw.Draw(th)
        td.ellipse((120, 100, 480, 460), outline=accent, width=14)
        for r in (80, 130, 180):
            td.arc((300 - r, 280 - r, 300 + r, 280 + r), 200, 340, fill=accent, width=16)
        td.rectangle((0, 500, 600, 600), fill=accent)
        f = font(36)
        box = td.textbbox((0, 0), name, font=f)
        td.text(((600 - (box[2]-box[0])) / 2, 525), name, font=f, fill=(255, 255, 255))
    else:
        b = Image.open(OUT / f"provider-{key}.jpg").convert("RGB")
        b.thumbnail((600, 540), Image.LANCZOS)
        th.paste(b, ((600 - b.width) // 2, 0))
        td = ImageDraw.Draw(th)
        td.rectangle((0, 540, 600, 600), fill=accent)
        f = font(32)
        box = td.textbbox((0, 0), name, font=f)
        td.text(((600 - (box[2]-box[0])) / 2, 552), name, font=f, fill=(255, 255, 255))
    th.save(OUT / f"{key}-thumb.jpg", "JPEG", quality=88, optimize=True)
    print(key, (OUT / f"{key}-hero.jpg").stat().st_size, (OUT / f"{key}-thumb.jpg").stat().st_size)
