import pathlib, re

FORWHO = {
    "articles/docomo-hikari.html": "ドコモスマホを使っていて、セット割と全国対応を重視する人",
    "articles/gmo-access.html": "工事なしで光回線を乗り換えたい人",
    "articles/softbank-hikari.html": "ソフトバンク／ワイモバイルのスマホを使っている人",
    "articles/flets-hikari.html": "エリアの広さと回線の安定性を重視する人",
    "articles/nuro-hikari.html": "とにかく速さを優先したい人／ゲーム・4K動画を楽しむ人",
    "articles/au-hikari.html": "au／UQユーザーで、安定した速度を求める人",
}

for name, who in FORWHO.items():
    p = pathlib.Path(name)
    s = p.read_text(encoding="utf-8")
    s = re.sub(r'<li><strong>向いている</strong>：.*?</li>',
               f'<li><strong>向いている</strong>：{who}</li>', s, count=1)
    p.write_text(s, encoding="utf-8")
    print("fixed", name)
