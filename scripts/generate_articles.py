import pathlib, json, html

BASE = "https://burattom.github.io/osechi-guide/"
GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-FVZHH3RMRT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-FVZHH3RMRT');
</script>
"""

OSECHI_LINK = "https://px.a8.net/svt/ejp?a8mat=4BGTLG+1UOM2Q+1ZWM+BZGEQ"
KANI_LINK = "https://px.a8.net/svt/ejp?a8mat=4BGTLG+1WGWW2+1ZWM+66H9E"

ARTICLES = [
    {
        "file": "articles/osechi-souba.html", "cat": "おせち相場", "img": "osechi-hero.jpg",
        "title": "おせcht 値段 相場｜一段・二段・三段の目安と早割の差",
        "title_fixed": "おせち 値段 相場｜一段・二段・三段の目安と早割の差",
        "desc": "おせち通販の価格相場を一段・二段・三段別に整理。早割でどう変わるか、家族の人数に合う選び方も解説します。",
        "h1": "おせち 値段 相場｜一段・二段・三段の目安と早割の差",
        "body": """
  <div class="lead"><strong>結論：</strong>通販おせちの価格は<strong>一段ものが3,000〜5,000円、二段ものが8,000〜12,000円、三段ものが15,000〜20,000円</strong>が目安です。早割なら同じおせちがさらに安くなります。</div>

  <h2>段数別の価格目安</h2>
  <table><thead><tr><th>段数</th><th>価格の目安</th><th>向いている人</th></tr></thead><tbody>
    <tr><td>一段もの</td><td>3,000〜5,000円</td><td>1〜2人・少量ずつ</td></tr>
    <tr><td>二段もの</td><td>8,000〜12,000円</td><td>2〜3人・バランス重視</td></tr>
    <tr><td>三段もの</td><td>15,000〜20,000円</td><td>3〜4人・来客あり</td></tr>
  </tbody></table>
  <p>あくまで一般的な通販の目安です。料亭監修や特定の食材を使った高級重では、これより高くなる場合もあります。</p>

  <h2>早割で価格はどう変わる？</h2>
  <p>匠本舗のおせちは、9月30日・10月31日・12月10日の3段階で早割が設定されています。同じ商品でも、注文する時期が遅いほど価格は上がります。<strong>11月下旬なら第3弾の期限内</strong>なので、まだ割引価格で購入できます。</p>

  <h2>価格だけで選ばないために</h2>
  <p>「安いから一段ものにした」ものの、年始に来客があって足りなくなるケースがあります。価格を見る前に、<strong>人数＋1人分</strong>を目安に段数を決めると失敗が減ります。</p>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>おせちはいつ頃買うのが安い？</dt><dd>早割の第1弾（9月末）が最安です。11月下旬なら第3弾（12月10日まで）が狙い目です。</dd>
    <dt>一段ものでも十分？</dt><dd>1〜2人で少量ずつ楽しむなら十分です。来客の可能性があるなら二段以上を選ぶのが安心です。</dd>
    <dt>価格と総重量はどちらを見る？</dt><dd>両方見るのがおすすめです。段数が同じでも総重量でボリュームが変わります。</dd>
  </dl>
""",
        "cta": OSECHI_LINK, "cta_text": "早割価格を公式サイトで確認する →", "related": [("料亭おせちの選び方", "osechi.html"), ("おせち早割2026", "osechi-saitei.html")],
    },
    {
        "file": "articles/osechi-yoyaku.html", "cat": "おせち予約", "img": "osechi-hero.jpg",
        "title": "おせち 予約 いつまで？2026年の締切と配送日の決め方",
        "title_fixed": "おせち 予約 いつまで？2026年の締切と配送日の決め方",
        "desc": "おせちの予約締切はいつまで？2026年の早割スケジュールと、12月31日に間に合う配送日の設定方法を解説します。",
        "h1": "おせち 予約 いつまで？2026年の締切と配送日の決め方",
        "body": """
  <div class="lead"><strong>結論：</strong>おせちの予約は<strong>12月10日頃まで</strong>が狙い目です。それ以降は価格が上がり、配送日の指定も難しくなります。</div>

  <h2>予約の締切と早割スケジュール</h2>
  <table><thead><tr><th>区分</th><th>締切</th><th>状態（11月下旬時点）</th></tr></thead><tbody>
    <tr><td>早割第1弾</td><td>9月30日</td><td>終了</td></tr>
    <tr><td>早割第2弾</td><td>10月31日</td><td>終了</td></tr>
    <tr><td>早割第3弾</td><td>12月10日</td><td><strong>開催中</strong></td></tr>
    <tr><td>通常販売</td><td>12月中旬〜</td><td>価格アップ</td></tr>
  </tbody></table>

  <h2>12月31日に間に合う配送日</h2>
  <p>冷凍おせちは解凍に丸1日かかります。食べる前日、<strong>12月30日の朝に冷蔵庫へ移す</strong>想定で、配送は12月29〜30日着を指定するのが安心です。年末は配送が混雑するため、早めに予約を済ませておきましょう。</p>

  <h2>予約前に確認すること</h2>
  <ul>
    <li>早割の締切日が過ぎていないか</li>
    <li>家族の人数に合う段数・総重量か</li>
    <li>配送日を指定できるか</li>
    <li>解凍手順が記載されているか</li>
  </ul>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>12月10日を過ぎたら予約できない？</dt><dd>できますが、早割価格ではなく通常価格になります。</dd>
    <dt>配送日は指定できる？</dt><dd>早い時期の予約ほど指定しやすいです。年末が近づくと枠が埋まります。</dd>
  </dl>
""",
        "cta": OSECHI_LINK, "cta_text": "早割価格を確認する →", "related": [("おせち早割2026", "osechi-saitei.html"), ("おせち解凍の方法", "osechi-kaihou.html")],
    },
    {
        "file": "articles/kani-tabekata.html", "cat": "かに食べ方", "img": "kani-hero.jpg",
        "title": "かに 食べ方｜鍋・焼き・刺身の上手な楽しみ方と解凍のコツ",
        "title_fixed": "かに 食べ方｜鍋・焼き・刺身の上手な楽しみ方と解凍のコツ",
        "desc": "かにの食べ方を鍋・焼き・刺身別に解説。解凍のコツや内容量の目安もまとめました。",
        "h1": "かに 食べ方｜鍋・焼き・刺身の上手な楽しみ方と解凍のコツ",
        "body": """
  <div class="lead"><strong>結論：</strong>かには<strong>前日に冷蔵庫で解凍し、当日に冷水で洗って水気を切る</strong>だけで、鍋でも焼きでも美味しく食べられます。</div>

  <h2>食べ方別のコツ</h2>
  <table><thead><tr><th>食べ方</th><th>コツ</th></tr></thead><tbody>
    <tr><td>鍋</td><td>弱火でじっくり。煮立てすぎると身が固くなる</td></tr>
    <tr><td>焼き</td><td>網で両面を焼き、出た水分を飛ばす</td></tr>
    <tr><td>刺身</td><td>完全に解凍する少し前、中心が少し残る状態が食べやすい</td></tr>
  </tbody></table>

  <h2>解凍の基本</h2>
  <ol>
    <li>前日に冷凍から冷蔵庫へ移す</li>
    <li>当日、冷水で軽く洗って水気を切る</li>
    <li>食べる直前に調理する</li>
  </ol>
  <p>常温解凍は身が水っぽくなる原因です。急ぐ場合は袋のまま氷水に浸す方法もあります。</p>

  <h2>内容量の目安</h2>
  <p>1人あたり500〜700gが目安です。2人で鍋と焼きの両方を楽しむなら1.5〜2.0kg、3〜4人で囲むなら2.5〜3.5kgが安心です。</p>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>かにみそはどう食べる？</dt><dd>甲羅に移して弱火で温め、酒を少し加えると食べやすくなります。</dd>
    <dt>残ったかにの保存は？</dt><dd>解後は当日中に食べ切るのが基本です。食べる分だけ解凍するのがおすすめです。</dd>
  </dl>
""".replace("解後", "解凍後"),
        "cta": KANI_LINK, "cta_text": "かにの内容量・価格を確認する →", "related": [("かにの失敗しない選び方", "kani.html"), ("かにの内容量の目安", "kani-ryo.html")],
    },
]


def build(a):
    title = a["title_fixed"]
    desc = a["desc"]
    url = BASE + a["file"]
    hero = f'{BASE}assets/{a["img"]}'
    cta = a["cta"]
    note = '<p class="cta-note">※ リンク先は広告主の公式サイトです（アフィリエイトリンク）</p>'
    cta_html = (f'<a class="cta" href="{cta}" rel="nofollow sponsored" target="_blank">{a["cta_text"]}</a>\n  {note}')
    cta_top = f'<div class="cta-top"><p style="margin:18px 0 0"><a class="cta" href="{cta}" rel="nofollow sponsored" target="_blank" style="margin:0">{a["cta_text"]}</a></p>\n  {note}</div>'
    body = a["body"]
    body = body.replace("<h2>よくある質問</h2>", cta_html + "\n\n  <h2>よくある質問</h2>", 1)
    body = body.replace("<div class=\"lead\">", "<div class=\"lead\">", 1)
    # insert top CTA after lead
    idx = body.find("</div>", body.find('<div class="lead">'))
    body = body[:idx+6] + "\n  " + cta_top + body[idx+6:]
    # insert final CTA before まとめ or 関連記事
    marker = "<h2>関連記事</h2>"
    body = body.replace(marker, cta_html + "\n\n  " + marker, 1)

    related = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in a["related"])
    faqs = __import__("re").findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", body, __import__("re").S)
    clean = lambda x: html.escape(__import__("re").sub(r"<[^>]+>", "", x).strip())
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": title, "description": desc, "url": url, "image": hero,
         "datePublished": "2026-11-25", "dateModified": "2026-11-25",
         "author": {"@type": "Organization", "name": "年末ごちそうガイド"},
         "publisher": {"@type": "Organization", "name": "年末ごちそうガイド"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(ans)}} for q, ans in faqs]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": a["cat"], "item": url}]},
    ]}

    return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../style.css">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:site_name" content="年末ごちそうガイド">
<meta property="og:locale" content="ja_JP">
<meta property="og:image" content="{hero}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
{GA}</head>
<body>

<header class="site-header">
  <div class="inner">
    <a class="logo" href="../index.html">年末ごちそう<span>ガイド</span></a>
    <nav class="nav">
      <a href="../index.html">ホーム</a>
      <a href="osechi.html">おせち</a>
      <a href="kani.html">かに</a>
      <a href="../about.html">当サイトについて</a>
    </nav>
  </div>
</header>

<div class="disclosure"><div class="inner">このページはアフィリエイト広告を含みます。リンクから購入すると当サイトに報酬が発生する場合があります。</div></div>

<main class="container">

<nav class="breadcrumb" aria-label="パンくずリスト">
  <a href="../index.html">ホーム</a> <span aria-hidden="true">›</span> <span>{a["cat"]}</span>
</nav>

<article class="article">

  <h1>{a["h1"]}</h1>
  <div class="meta">最終更新：2026年11月25日 ｜ カテゴリ：{a["cat"]}</div>
  <img class="article-hero" src="../assets/{a["img"]}" alt="{a["cat"]}" width="1200" height="800">

{body}

{cta_html}

<h2>関連記事</h2>
  <ul>{related}</ul>

</article>

</main>

<footer class="site-footer">
  <div class="inner">&copy; 年末ごちそうガイド ｜ <a href="../about.html">アフィリエイト開示・プライバシーポリシー</a></div>
</footer>

<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</body>
</html>
'''

if __name__ == "__main__":
    for a in ARTICLES:
        p = pathlib.Path(a["file"])
        p.write_text(build(a), encoding="utf-8")
        print("created", p)
