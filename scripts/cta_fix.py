import pathlib, re
for p in sorted(pathlib.Path("articles").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    if s.count('class="cta"') >= 3:
        continue
    m = re.search(r'<a class="cta" href="([^"]+)"([^>]*)>.*?</a>\s*<p class="cta-note">.*?</p>', s, re.S)
    if not m:
        continue
    href, attrs = m.group(1), m.group(2)
    text = re.search(r'<a class="cta"[^>]*>(.*?)</a>', m.group(0), re.S).group(1)
    note = '<p class="cta-note">※ リンク先は広告主の公式サイトです（アフィリエイトリンク）</p>'
    snippet = f'<a class="cta" href="{href}"{attrs}>{text}</a>\n  {note}\n\n  '
    s = s.replace("<h2>まとめ</h2>", snippet + "<h2>まとめ</h2>", 1)
    p.write_text(s, encoding="utf-8")
    print("fixed", p.name)
