import re, html, pathlib, json

ROOT = pathlib.Path(__file__).parent
BASE = "https://burattom.github.io/osechi-guide/"
OGP_IMG = BASE + "sns/assets/osechi-banner-250-1.jpg"

cta_text = {
    "articles/osechi.html": "早割価格を公式サイトで確認する →",
    "articles/osechi-saitei.html": "第3弾の早割価格を確認する →",
    "articles/osechi-kaihou.html": "早割価格を公式サイトで確認する →",
    "articles/kani.html": "内容量・価格を公式サイトで確認する →",
    "articles/kani-ryo.html": "内容量・価格を公式サイトで確認する →",
    "articles/kani-kaihou.html": "内容量・価格を公式サイトで確認する →",
}

related = {
    "articles/osechi.html": [("おせち早割 2026｜いつまで？", "osechi-saitei.html"), ("おせち 解凍 方法｜冷蔵庫で何時間？", "osechi-kaihou.html")],
    "articles/osechi-saitei.html": [("料亭おせちの選び方", "osechi.html"), ("おせち 解凍 方法｜冷蔵庫で何時間？", "osechi-kaihou.html")],
    "articles/osechi-kaihou.html": [("料亭おせちの選び方", "osechi.html"), ("おせち早割 2026｜いつまで？", "osechi-saitei.html")],
    "articles/kani.html": [("かに 内容量の目安｜何kgで何人分？", "kani-ryo.html"), ("かに 解凍 方法｜冷蔵庫で何時間？", "kani-kaihou.html")],
    "articles/kani-ryo.html": [("かに通販の失敗しない選び方", "kani.html"), ("かに 解凍 方法｜冷蔵庫で何時間？", "kani-kaihou.html")],
    "articles/kani-kaihou.html": [("かに通販の失敗しない選び方", "kani.html"), ("かに 内容量の目安｜何kgで何人分？", "kani-ryo.html")],
}

compare = {
    "articles/osechi.html": """
  <h2>目的別の選び方</h2>
  <table>
    <thead><tr><th>目的</th><th>おすすめ</th><th>理由</th></tr></thead>
    <tbody>
      <tr><td>少しでも安く买いたい</td><td>早割第3弾（12/10まで）</td><td>同じおせちが割引価格で買える</td></tr>
      <tr><td>家族でしっかり食べたい</td><td>総重量3.0kg以上</td><td>来客分も含めて足りやすい</td></tr>
      <tr><td>味に失敗したくない</td><td>料亭監修・段数多め</td><td>和洋中のバリエーションで好みが分かれても残りにくい</td></tr>
    </tbody>
  </table>""".replace("买いたい", "買いたい"),
    "articles/kani.html": """
  <h2>目的別の選び方</h2>
  <table>
    <thead><tr><th>目的</th><th>おすすめ</th><th>理由</th></tr></thead>
    <tbody>
      <tr><td>2人で気軽に食べる</td><td>内容量1.5〜2.0kg</td><td>鍋と焼きの両方を楽しめる</td></tr>
      <tr><td>贈答・まとめ買い</td><td>3kg以上</td><td>単価が下がり送料もお得</td></tr>
      <tr><td>鮮度重視</td><td>急速冷凍・解凍手順明記</td><td>状態よく届く</td></tr>
    </tbody>
  </table>""",
}

files = sorted(ROOT.glob("articles/*.html")) + [ROOT / "index.html", ROOT / "about.html"]

for f in files:
    rel = f.relative_to(ROOT).as_posix()
    s = f.read_text(encoding="utf-8")
    url = BASE + rel
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    desc_m = re.search(r'<meta name="description" content="(.*?)">', s, re.S)
    desc = desc_m.group(1) if desc_m else ""

    # canonical / OGP / Twitter
    head_extra = f'''<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:site_name" content="年末ごちそうガイド">
<meta property="og:locale" content="ja_JP">
<meta property="og:image" content="{OGP_IMG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
'''
    if 'rel="canonical"' not in s:
        s = s.replace("</head>", head_extra + "</head>")

    if rel.startswith("articles/"):
        # JSON-LD Article + FAQPage
        qs = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", s, re.S)
        clean = lambda x: html.escape(re.sub(r"<[^>]+>", "", x).strip())
        qa = [{"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in qs]
        ld = {
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "Article", "headline": title, "description": desc, "url": url,
                 "image": OGP_IMG, "datePublished": "2026-11-25", "dateModified": "2026-11-25",
                 "author": {"@type": "Organization", "name": "年末ごちそうガイド"},
                 "publisher": {"@type": "Organization", "name": "年末ごちそうガイド"}},
                {"@type": "FAQPage", "mainEntity": qa},
            ],
        }
        if "application/ld+json" not in s:
            s = s.replace("</body>", '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n</body>")

        # CTA improvements and 3 placements
        m = re.search(r'<a class="cta" href="([^"]+)"([^>]*)>.*?</a>\s*<p class="cta-note">.*?</p>', s, re.S)
        if m:
            href, attrs = m.group(1), m.group(2)
            note = '<p class="cta-note">※ リンク先は広告主の公式サイトです（アフィリエイトリンク）</p>'
            new_text = cta_text.get(rel, "公式サイトで確認する →")
            cta_bottom = f'<a class="cta" href="{href}"{attrs}>{new_text}</a>\n  {note}'
            s = s[:m.start()] + cta_bottom + s[m.end():]

            cta_top = f'''<p style="margin:18px 0 0"><a class="cta" href="{href}"{attrs} style="margin:0">{new_text}</a></p>
  {note}'''
            # after lead div
            lead = re.search(r'<div class="lead">.*?</div>', s, re.S)
            if lead and "cta-top" not in s:
                s = s[:lead.end()] + '\n  <div class="cta-top">' + cta_top + '</div>' + s[lead.end():]

            cta_mid = f'''<a class="cta" href="{href}"{attrs}>{new_text}</a>
  {note}'''
            anchor = "<h2>よくある質問</h2>"
            if anchor in s and s.count('class="cta"') < 3:
                s = s.replace(anchor, cta_mid + "\n\n  " + anchor, 1)

        # related links + comparison
        if rel in related:
            links = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in related[rel])
            block = '<h2>関連記事</h2>\n  <ul>' + links + '</ul>'
            s = s.replace("</article>", block + "\n\n</article>")
        if rel in compare:
            s = s.replace("<h2>よくある質問</h2>", compare[rel] + "\n\n  <h2>よくある質問</h2>")

    f.write_text(s, encoding="utf-8")
    print("updated", rel)
