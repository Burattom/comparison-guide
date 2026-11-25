import pathlib

OLD = "https://burattom.github.io/osechi-guide/sns/assets/osechi-banner-250-1.jpg"
BASE = "https://burattom.github.io/osechi-guide/assets/"

for p in sorted(pathlib.Path(".").glob("*.html")) + sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    if OLD not in s:
        continue
    img = "kani-hero.jpg" if "kani" in p.name else "osechi-hero.jpg"
    s = s.replace(OLD, BASE + img)
    p.write_text(s, encoding="utf-8")
    print("updated", p, img)
