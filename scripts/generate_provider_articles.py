import pathlib, json, html, re

BASE = "https://burattom.github.io/comparison-guide/"
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">\n'
GA = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-FVZHH3RMRT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-FVZHH3RMRT');
</script>
'''

LINKS = {
    "docomo": "https://px.a8.net/svt/ejp?a8mat=4BGTLG+1UOLAY+1ZWM+60H7M",
    "gmo": "https://px.a8.net/svt/ejp?a8mat=4BGTLO+31JTMQ+50+6M5TEQ",
    "softbank": "https://px.a8.net/svt/ejp?a8mat=4BGTLR+A4FLU+348K+1BP8ZM",
    "softbank2": "https://px.a8.net/svt/ejp?a8mat=4BGTLR+2DSQQ+50+740TK2",
    "flets": "https://px.a8.net/svt/ejp?a8mat=4BGTLR+FHC1U+1MWA+1TJ6K2",
}

ARTICLES = [
    dict(file="articles/docomo-hikari.html", slug="docomo-hikari", cat="ドコモ光", name="ドコモ光", type="光コラボ（NTTフレッツ網）",
         down="629 Mbps", up="480 Mbps", ping="21.0 ms", night="夜間低下 -42%（BNR・ドコモ光）",
         good=["ドコモスマホとのセット割", "全国で利用可能", "転用・事業者変更で工事なし乗り換え"],
         bad=["光コラボのため夜間の混雑影響を受けやすい", "Pingは独自回線よりやや高い"],
         forwho="ドコモスマホを使っていて、セット割と全国対応を重視する人",
         check=["セット割の適用条件", "特典の受取時期", "更新月と違約金"],
         cta=LINKS["docomo"], cta_text="ドコモ光の条件を確認する →",
         extra="GMOとくとくBB経由なら、ドコモ光単体・ドコモでんきセット・dカードセット・3点セットで特典内容が異なります。"),
    dict(file="articles/gmo-access.html", slug="gmo-access", cat="GMO光アクセス", name="GMO光アクセス", type="光コラボ（NTTフレッツ網）",
         down="630 Mbps", up="525 Mbps", ping="19.2 ms", night="夜間低下 -22%（BNR・GMOとくとくBB）",
         good=["転用・事業者変更・新規開通がすべて対象", "工事なしで乗り換えやすい", "全国対応"],
         bad=["独自回線ほどの速度は出にくい", "特典条件の確認が必要"],
         forwho="工事なしで光回線を乗り換えたい人",
         check=["提供エリア", "転用・事業者変更の可否", "特典の受取条件"],
         cta=LINKS["gmo"], cta_text="GMO光アクセスの条件を確認する →",
         extra="GMOとくとくBBの実測下りは630Mbps台。光コラボの中では速い部類ですが、夜間は混雑の影響を受けます。"),
    dict(file="articles/softbank-hikari.html", slug="softbank-hikari", cat="SoftBank光", name="SoftBank光", type="光コラボ（NTTフレッツ網）",
         down="580 Mbps", up="471 Mbps", ping="17.1 ms", night="夜間低下 -24%（BNR・SoftBank）",
         good=["ソフトバンク・ワイモバイルとのセット割", "全国対応", "代理店により特典の受け取りやすさを訴求"],
         bad=["光コラボのため夜間の混雑影響がある", "代理店ごとに条件が異なる"],
         forwho="ソフトバンク／ワイモバイルのスマホを使っている人",
         check=["セット割の対象", "特典の受取期限", "代理店ごとの条件差"],
         cta=LINKS["softbank"], cta_text="SoftBank光の条件を確認する →",
         extra="当サイトではSoftBank光（NEXT）とGMOとくとくBBソフトバンク光の2つの案件を扱っています。条件を比べてから申し込むのがおすすめです。",
         cta2=LINKS["softbank2"], cta2_text="GMOソフトバンク光の条件も見る →"),
    dict(file="articles/flets-hikari.html", slug="flets-hikari", cat="フレッツ光", name="フレッツ光", type="NTTフレッツ回線（光コラボの元）",
         down="407 Mbps", up="300 Mbps", ping="23.9 ms", night="プロバイダにより夜低下 -39%〜-52%（BNR）",
         good=["全国の光回線基盤でエリアが広い", "回線の安定性", "光コラボ各社がこの回線を利用"],
         bad=["光コラボ系の中では実測速度が控えめ", "プロバイダ選択で速度が変わる", "窓口ごとに特典差が大きい"],
         forwho="エリアの広さと回線の安定性を重視する人",
         check=["プロバイダ／接続方式（IPoEかPPPoEか）", "窓口ごとの特典条件", "工事日"],
         cta=LINKS["flets"], cta_text="フレッツ光の申込窓口を確認する →",
         extra="フレッツ光ネクストの実測は下り407Mbps前後。同じフレッツ網でもプロバイダや接続方式で速度が変わるため、窓口選びが重要です。"),
    dict(file="articles/nuro-hikari.html", slug="nuro-hikari", cat="NURO光", name="NURO光", type="独自回線",
         down="976 Mbps", up="782 Mbps", ping="11.5 ms", night="夜間低下なし（BNR）",
         good=["実測速度がトップクラス", "上りも速くテレワーク向き", "Pingが低くゲーム向き"],
         bad=["提供エリアが一部地域に限定", "工事が必要な場合がある", "契約期間の縛りに注意"],
         forwho="とにかく速さを優先したい人／ゲーム・4K動画を楽しむ人",
         check=["自宅が提供エリア内か", "10ギガプランの料金", "契約期間と解除料"],
         cta=None, cta_text="NURO光の公式サイトでエリアを確認 →",
         cta_url="https://www.sonynetwork.co.jp/nurohikari/",
         extra="当サイトはNURO光のアフィリエイト案件を扱っていません。リンクは公式サイトです。速さ最優先なら有力候補ですが、まずエリア確認から。"),
    dict(file="articles/au-hikari.html", slug="au-hikari", cat="auひかり", name="auひかり", type="独自回線",
         down="706 Mbps", up="622 Mbps", ping="16.3 ms", night="夜間低下 -5%（BNR）",
         good=["独自回線で夜間も安定", "au・UQとのセット割", "上り速度が速い"],
         bad=["関西・中部など一部エリアは提供外", "工事が必要", "セット割はauユーザー向け"],
         forwho="au／UQユーザーで、安定した速度を求める人",
         check=["提供エリア（関西・中部は対象外が多い）", "工事日", "セット割の条件"],
         cta=None, cta_text="auひかりの公式サイトでエリアを確認 →",
         cta_url="https://www.au.com/internet/au-hikari/",
         extra="当サイトはauひかりのアフィリエイト案件を扱っていません。リンクは公式サイトです。独自回線で夜間の安定を重視するなら候補になります。"),
]


def build(a):
    url = BASE + a["file"]
    hero = BASE + "assets/hikari-hero.jpg"
    title = f'{a["name"]}の実測速度と選び方｜{a["type"]}のメリット・デメリット'
    desc = f'{a["name"]}の実測速度（下り{a["down"]}／上り{a["up"]}）、回線種別、向いている人、申し込み前の確認点を解説します。'
    cta_url = a["cta"] or a["cta_url"]
    cta_html = f'<a class="cta" href="{cta_url}" rel="nofollow sponsored" target="_blank">{a["cta_text"]}</a>\n  <p class="cta-note">※ リンク先は公式サイトです。当サイトの提携案件でない場合は報酬は発生しません。</p>'

    good = "".join(f"<li>{x}</li>" for x in a["good"])
    bad = "".join(f"<li>{x}</li>" for x in a["bad"])
    checks = "".join(f"<li>{x}</li>" for x in a["check"])
    cta2 = ""
    if a.get("cta2"):
        cta2 = f'<p><a href="{a["cta2"]}" rel="nofollow sponsored" target="_blank">{a["cta2_text"]}</a></p>'

    faq = [
        (f'{a["name"]}はどんな回線？', f'{a["type"]}です。実測の下りは{a["down"]}、上りは{a["up"]}、Pingは{a["ping"]}前後（みんなのネット回線速度・直近3か月平均）。'),
        ("実測速度は保証される？", "いいえ。測定環境・時間帯・機器によって変わります。公称値ではなく目安としてご覧ください。"),
        (f'{a["name"]}は誰に向いている？', a["forwho"]),
        ("申し込み前に何を確認すべき？", "・".join(a["check"]) + "を確認してください。"),
    ]
    faq_html = "".join(f"    <dt>{q}</dt>\n    <dd>{ans}</dd>\n" for q, ans in faq)
    clean = lambda x: html.escape(re.sub(r"<[^>]+>", "", x).strip())
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": title, "description": desc, "url": url, "image": hero,
         "datePublished": "2026-11-25", "dateModified": "2026-11-25",
         "author": {"@type": "Organization", "name": "比較ガイド"},
         "publisher": {"@type": "Organization", "name": "比較ガイド"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(v)}} for q, v in faq]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "光回線比較", "item": BASE + "articles/gmo-hikari.html"},
            {"@type": "ListItem", "position": 3, "name": a["cat"], "item": url}]},
    ]}

    related = '<li><a href="gmo-hikari.html">光回線5社の比較表</a></li><li><a href="docomo-hikari.html">ドコモ光の選び方</a></li>'

    return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{FONT}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../style.css">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:site_name" content="比較ガイド">
<meta property="og:locale" content="ja_JP">
<meta property="og:image" content="{hero}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
{GA}</head>
<body>

<header class="site-header">
  <div class="inner">
    <a class="logo" href="../index.html">比較<span>ガイド</span></a>
    <nav class="nav">
      <a href="../index.html">ホーム</a>
      <a href="docomo-hikari.html">光回線</a>
      <a href="gmo-hikari.html">回線比較</a>
      <a href="goods-buyback.html">グッズ買取</a>
      <a href="../about.html">当サイトについて</a>
    </nav>
  </div>
</header>

<div class="disclosure"><div class="inner">このページはアフィリエイト広告（A8.net）を含みます。リンクから申し込むと報酬が発生する場合があります。</div></div>

<main class="container">

<nav class="breadcrumb" aria-label="パンくずリスト">
  <a href="../index.html">ホーム</a> <span aria-hidden="true">›</span> <a href="gmo-hikari.html">光回線比較</a> <span aria-hidden="true">›</span> <span>{a["cat"]}</span>
</nav>

<article class="article">

  <h1>{title}</h1>
  <div class="meta">最終更新：2026年11月25日 ｜ カテゴリ：光回線</div>
  <img class="article-hero" src="../assets/hikari-hero.jpg" alt="{a["name"]}の比較イメージ" width="1200" height="800">

  <div class="lead"><strong>結論：</strong>{a["name"]}は<strong>{a["type"]}</strong>です。実測の下りは<strong>{a["down"]}</strong>、上り<strong>{a["up"]}</strong>、Ping<strong>{a["ping"]}</strong>前後。{a["forwho"]}に向いています。</div>

  <h2>実測データ</h2>
  <table>
    <thead><tr><th>項目</th><th>数値</th></tr></thead>
    <tbody>
      <tr><td>回線種別</td><td>{a["type"]}</td></tr>
      <tr><td>下り平均</td><td>{a["down"]}</td></tr>
      <tr><td>上り平均</td><td>{a["up"]}</td></tr>
      <tr><td>Ping平均</td><td>{a["ping"]}</td></tr>
      <tr><td>夜間の傾向</td><td>{a["night"]}</td></tr>
    </tbody>
  </table>
  <p class="cta-note">出典：みんなのネット回線速度（直近3か月平均）／BNRスピードテスト（直近60日）。環境により変動するため、回線能力を保証する数値ではありません。</p>

  <h2>メリット・デメリット</h2>
  <h3>メリット</h3>
  <ul>{good}</ul>
  <h3>デメリット・注意点</h3>
  <ul>{bad}</ul>

  {cta_html}
  {cta2}
  <p>{a["extra"]}</p>

  <h2>申し込み前に確認すること</h2>
  <ul>{checks}</ul>

  <h2>よくある質問</h2>
  <dl class="faq">
{faq_html}  </dl>

  <h2>まとめ</h2>
  <p>{a["name"]}は{a["forwho"]}に向いた回線です。回線種別と実測速度の傾向を踏まえたうえで、公式サイトで最新のエリア・条件を確認してください。</p>

  <p><a href="gmo-hikari.html">→ 光回線5社の比較表を見る</a></p>

<h2>関連記事</h2>
  <ul>{related}</ul>

</article>

</main>

<footer class="site-footer">
  <div class="inner">&copy; 比較ガイド ｜ <a href="../about.html">アフィリエイト開示・プライバシーポリシー</a></div>
</footer>

<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</body>
</html>
'''

for a in ARTICLES:
    p = pathlib.Path(a["file"])
    p.write_text(build(a), encoding="utf-8")
    print("created", p)
