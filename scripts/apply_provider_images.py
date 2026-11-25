import pathlib, re

H = {
    "articles/docomo-hikari.html": "docomo-hero.jpg",
    "articles/gmo-access.html": "gmo-hero.jpg",
    "articles/softbank-hikari.html": "softbank-hero.jpg",
    "articles/flets-hikari.html": "flets-hero.jpg",
    "articles/nuro-hikari.html": "nuro-hero.jpg",
    "articles/au-hikari.html": "au-hero.jpg",
}

for name, img in H.items():
    p = pathlib.Path(name)
    s = p.read_text(encoding="utf-8")
    s = s.replace("../assets/hikari-hero.jpg", f"../assets/{img}")
    s = s.replace("https://burattom.github.io/comparison-guide/assets/hikari-hero.jpg",
                  f"https://burattom.github.io/comparison-guide/assets/{img}")
    p.write_text(s, encoding="utf-8")
    print("article", name, img)

# index cards
p = pathlib.Path("index.html")
s = p.read_text(encoding="utf-8")
CARDS = {
    'href="articles/docomo-hikari.html"': "docomo-thumb.jpg",
    'href="articles/gmo-access.html"': "gmo-thumb.jpg",
    'href="articles/softbank-hikari.html"': "softbank-thumb.jpg",
    'href="articles/flets-hikari.html"': "flets-thumb.jpg",
    'href="articles/nuro-hikari.html"': "nuro-thumb.jpg",
    'href="articles/au-hikari.html"': "au-thumb.jpg",
}
for href, thumb in CARDS.items():
    idx = s.find(href)
    if idx < 0:
        continue
    seg = s[idx:idx + 700]
    seg2 = re.sub(r'src="assets/[^"]+"', f'src="assets/{thumb}"', seg, count=1)
    s = s[:idx] + seg2 + s[idx + 700:]
p.write_text(s, encoding="utf-8")
print("index updated")
