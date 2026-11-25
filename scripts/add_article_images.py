import pathlib, re

MAP = {
    "osechi.html": ("osechi-hero.jpg", "料亭おせちの三段重と急須"),
    "osechi-saitei.html": ("osechi-hero.jpg", "おせち早割の料亭おせち"),
    "osechi-kaihou.html": ("osechi-hero.jpg", "おせちの解凍イメージ"),
    "kani.html": ("kani-hero.jpg", "ボイルずわいがにの盛り合わせ"),
    "kani-ryo.html": ("kani-hero.jpg", "かにの内容量の目安"),
    "kani-kaihou.html": ("kani-hero.jpg", "かにの解凍イメージ"),
}

for name, (img, alt) in MAP.items():
    p = pathlib.Path("articles") / name
    s = p.read_text(encoding="utf-8")
    if 'class="article-hero"' in s:
        print("skip", name)
        continue
    m = re.search(r'(<div class="meta">.*?</div>)', s, re.S)
    if not m:
        print("no meta", name)
        continue
    tag = f'\n  <img class="article-hero" src="../assets/{img}" alt="{alt}">'
    s = s[:m.end()] + tag + s[m.end():]
    p.write_text(s, encoding="utf-8")
    print("updated", name)
