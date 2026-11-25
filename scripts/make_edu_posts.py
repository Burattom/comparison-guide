from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("sns/assets")
OUT.mkdir(exist_ok=True)
FONT = "C:\\Windows\\Fonts\\NotoSansJP-VF.ttf"
W = H = 1080
NAVY = (22, 50, 79)
TEAL = (14, 116, 144)
BG = (244, 247, 250)
WHITE = (255, 255, 255)
MUTED = (97, 112, 128)
GOLD = (201, 162, 39)


def font(size):
    return ImageFont.truetype(FONT, size)


def center(d, y, text, size, fill, x=W // 2):
    f = font(size)
    box = d.textbbox((0, 0), text, font=f)
    d.text((x - (box[2] - box[0]) / 2, y), text, font=f, fill=fill)


def base(title, subtitle):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 110), fill=NAVY)
    d.text((60, 32), "比較ガイド", font=font(38), fill=WHITE)
    d.rounded_rectangle((880, 34, 1020, 76), radius=20, fill=TEAL)
    center(d, 40, "教育", 28, WHITE, 950)
    center(d, 160, title, 58, NAVY)
    center(d, 250, subtitle, 30, MUTED)
    return img, d


def rows(d, items, start=340):
    y = start
    for i, (num, head, desc) in enumerate(items, 1):
        d.rounded_rectangle((80, y, 1000, y + 170), radius=18, fill=WHITE)
        d.ellipse((110, y + 45, 190, y + 125), fill=TEAL)
        center(d, y + 62, str(num), 46, WHITE, 150)
        d.text((225, y + 32), head, font=font(42), fill=NAVY)
        d.text((225, y + 96), desc, font=font(28), fill=MUTED)
        y += 195


def footer(img, d):
    d.rectangle((0, H - 100, W, H), fill=NAVY)
    center(d, H - 78, "詳しい比較記事はプロフィールリンクから", 32, WHITE)


# 1. 乗り換えで確認する3つ
img, d = base("光回線の乗り換え", "失敗しないために確認する3つのこと")
rows(d, [
    (1, "工事費", "実質無料か、分割で残るか"),
    (2, "キャッシュバック", "受け取れる時期と条件"),
    (3, "契約期間", "更新月と違約金の有無"),
])
footer(img, d)
img.save(OUT / "edu-hikari-1080.png")

# 2. 転用・事業者変更・新規
img, d = base("回線の乗り換えの種類", "工事が必要かどうかで3つに分かれます")
rows(d, [
    (1, "転用", "NTT回線を他社サービスへ。工事不要が多い"),
    (2, "事業者変更", "他社回線から別事業者へ。工事不要が多い"),
    (3, "新規開通", "回線を新しく引く。工事が必要"),
])
footer(img, d)
img.save(OUT / "edu-tennyou-1080.png")

# 3. 買取の準備
img, d = base("グッズ買取のコツ", "査定額が上がりやすい3つの準備")
rows(d, [
    (1, "付属品を揃える", "箱・説明書・特典があるとプラス"),
    (2, "状態を記録", "傷や汚れを写真で残す"),
    (3, "複数社で比較", "得意ジャンルで査定額が変わる"),
])
footer(img, d)
img.save(OUT / "edu-kaitori-1080.png")

for f in ["edu-hikari-1080.png", "edu-tennyou-1080.png", "edu-kaitori-1080.png"]:
    print(f, (OUT / f).stat().st_size)
