import pathlib, re, json, html

CAT = {
    "osechi.html": "おせち", "osechi-saitei.html": "おせち早割", "osechi-kaihou.html": "おせち解凍",
    "kani.html": "かに", "kani-ryo.html": "かに内容量", "kani-kaihou.html": "かに解凍",
}

for name, cat in CAT.items():
    p = pathlib.Path("articles") / name
    s = p.read_text(encoding="utf-8")
    url = f"https://burattom.github.io/osechi-guide/articles/{name}"

    if 'class="breadcrumb"' not in s:
        bc = (f'<nav class="breadcrumb" aria-label="パンくずリスト">\n'
              f'  <a href="../index.html">ホーム</a> <span aria-hidden="true">›</span> <span>{cat}</span>\n'
              f'</nav>\n\n')
        s = s.replace('<main class="container">', '<main class="container">\n\n' + bc, 1)

    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if m:
        data = json.loads(m.group(1))
        if not any(n.get("@type") == "BreadcrumbList" for n in data.get("@graph", [])):
            data["@graph"].append({
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://burattom.github.io/osechi-guide/"},
                    {"@type": "ListItem", "position": 2, "name": cat, "item": url},
                ],
            })
        s = s[:m.start()] + '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>' + s[m.end():]

    # image dimensions + lazy for card thumbs
    s = re.sub(r'<img class="article-hero" src="\.\./assets/([^"]+)" alt="([^"]+)">',
               r'<img class="article-hero" src="../assets/\1" alt="\2" width="1200" height="800">', s)
    p.write_text(s, encoding="utf-8")
    print("updated", name)

# index: card thumbs + hero dimensions
p = pathlib.Path("index.html")
s = p.read_text(encoding="utf-8")
s = s.replace('<img class="hero-image" src="assets/osechi-hero.jpg" alt="料亭おせちの三段重と急須">',
              '<img class="hero-image" src="assets/osechi-hero.jpg" alt="料亭おせちの三段重と急須" width="1200" height="800">')
s = re.sub(r'<img class="card-thumb" src="assets/([^"]+)" alt="([^"]+)">',
           r'<img class="card-thumb" src="assets/\1" alt="\2" width="600" height="600" loading="lazy">', s)
p.write_text(s, encoding="utf-8")
print("updated index")
