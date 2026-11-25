import pathlib, re, html

print(f"{'file':<28} {'chars':>6} {'h2':>3} {'faq':>4} {'img':>4} {'alt':>4} {'title':>5}")
for p in sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    body = s[s.find("<article"):s.find("</article>")]
    text = re.sub(r"<[^>]+>", "", body)
    text = html.unescape(re.sub(r"\s+", "", text))
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    print(f"{p.name:<28} {len(text):>6} {body.count('<h2'):>3} {body.count('<dt>'):>4} {body.count('<img'):>4} {body.count('alt='):>4} {len(title):>5}")
