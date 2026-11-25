import pathlib
for p in sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    print(p.name, "cta=", s.count('class="cta"'), "ld=", "ld+json" in s, "canonical=", 'rel="canonical"' in s, "related=", "関連記事" in s)
