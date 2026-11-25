import pathlib

LINK = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">\n'

for p in [pathlib.Path("index.html"), pathlib.Path("about.html")] + sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    if "fonts.googleapis.com" in s:
        continue
    s = s.replace('<link rel="stylesheet" href="', LINK + '<link rel="stylesheet" href="', 1)
    p.write_text(s, encoding="utf-8")
    print("updated", p)
