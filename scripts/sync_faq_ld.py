import pathlib, re, html, json

for p in sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if not m:
        continue
    data = json.loads(m.group(1))
    qs = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", s, re.S)
    clean = lambda x: html.escape(re.sub(r"<[^>]+>", "", x).strip())
    faq = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}}
        for q, a in qs
    ]}
    for node in data.get("@graph", []):
        if node.get("@type") == "FAQPage":
            node.clear()
            node.update(faq)
    s = s[:m.start()] + '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>' + s[m.end():]
    p.write_text(s, encoding="utf-8")
    print(p.name, len(qs))
