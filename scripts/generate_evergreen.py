import pathlib
from generate_articles import build

DOCOMO = "https://px.a8.net/svt/ejp?a8mat=4BGTLO+3KLOZM+50+54MIOY"
GMO = "https://px.a8.net/svt/ejp?a8mat=4BGTLO+31JTMQ+50+6M5TEQ"
JANI = "https://px.a8.net/svt/ejp?a8mat=4BGTLO+32598I+3HXW+BWVTE"

ARTICLES = [
    {
        "file": "articles/docomo-hikari.html", "cat": "光回線", "img": "hikari-hero.jpg",
        "title_fixed": "ドコモ光 乗り換え｜工事費とキャッシュバックの確認ポイント",
        "desc": "ドコモ光へ乗り換える前に確認したい工事費・キャッシュバック・契約期間のポイントを整理しました。",
        "h1": "ドコモ光 乗り換え｜工事費とキャッシュバックの確認ポイント",
        "body": """
  <div class="lead"><strong>結論：</strong>光回線の乗り換えは<strong>「工事費の実質負担」「キャッシュバックの受取時期」「契約期間の縛り」</strong>の3点を先に確認すると失敗しません。</div>

  <h2>確認しておきたい3つのポイント</h2>
  <table><thead><tr><th>項目</th><th>確認すること</th></tr></thead><tbody>
    <tr><td>工事費</td><td>実質無料か、分割で残るか</td></tr>
    <tr><td>キャッシュバック</td><td>受け取れる時期と条件</td></tr>
    <tr><td>契約期間</td><td>更新月・違約金の有無</td></tr>
  </tbody></table>

  <h2>乗り換えの流れ</h2>
  <ol>
    <li>現在の回線の契約期間・違約金を確認する</li>
    <li>新しい回線の工事日を調整する</li>
    <li>開通後、旧回線を解約する</li>
  </ol>

  <h2>無料で比較から始める</h2>
  <p>いきなり契約せず、条件だけ確認したい場合は、各社の資料請求や無料相談を利用するのが安心です。A8.net経由なら申し込みで報酬が発生する案件もあります。</p>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>工事費はかかる？</dt><dd>キャンペーンで実質無料になる場合があります。条件は公式サイトで確認してください。</dd>
    <dt>乗り換えに期間はかかる？</dt><dd>開通まで数週間かかることが一般的です。解約のタイミングに注意しましょう。</dd>
  </dl>
""",
        "cta": DOCOMO, "cta_text": "ドコモ光のキャンペーンを確認する →", "related": [("GMO光アクセスの比較", "gmo-hikari.html"), ("おせち早割", "osechi-saitei.html")],
    },
    {
        "file": "articles/gmo-hikari.html", "cat": "光回線比較", "img": "hikari-hero.jpg",
        "title_fixed": "光回線 乗り換え 比較｜GMO光アクセスの申込前に見るポイント",
        "desc": "GMO光アクセスの乗り換えで確認したい料金・工事費・キャッシュバックの条件を比較しやすく整理しました。",
        "h1": "光回線 乗り換え 比較｜GMO光アクセスの申込前に見るポイント",
        "body": """
  <div class="lead"><strong>結論：</strong>光回線の乗り換えは<strong>月額料金だけでなく、工事費と特典の受取条件</strong>まで比べると満足度が変わります。</div>

  <h2>比較するときのチェックリスト</h2>
  <ul>
    <li>月額料金（戸建て／マンションで異なる）</li>
    <li>工事費の実質負担</li>
    <li>キャッシュバックの額と受取時期</li>
    <li>契約期間と違約金</li>
    <li>実測速度の口コミ</li>
  </ul>

  <h2>GMO光アクセスの特徴</h2>
  <p>GMO光アクセスは、転用・事業者変更・新規開通いずれも成果対象となるプログラムです。乗り換え時期に合わせて選びやすいのが特徴です。</p>

  <h2>まずは条件だけ確認する</h2>
  <p>契約を急がず、公式サイトで現在のキャンペーンと提供エリアを確認してから申し込むのが安心です。</p>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>事業者変更とは？</dt><dd>同じ光回線の設備を使ったまま、事業者だけを変える手続きです。工事が不要な場合があります。</dd>
    <dt>提供エリアは確認できる？</dt><dd>公式サイトのエリア確認ページで住所から調べられます。</dd>
  </dl>
""",
        "cta": GMO, "cta_text": "GMO光アクセスの条件を確認する →", "related": [("ドコモ光の比較", "docomo-hikari.html")],
    },
    {
        "file": "articles/goods-buyback.html", "cat": "グッズ買取", "img": "goods-hero.jpg",
        "title_fixed": "グッズ買取 相場｜売る前に比較したいポイントと手順",
        "desc": "グッズを買取に出す前に確認したい相場の見方・状態の確認・手続きの流れを解説します。",
        "h1": "グッズ買取 相場｜売る前に比較したいポイントと手順",
        "body": """
  <div class="lead"><strong>結論：</strong>グッズ買取は<strong>状態・付属品・需要</strong>の3点で査定額が変わります。まずは無料査定で比較するのがおすすめです。</div>

  <h2>査定額が変わる3つの要素</h2>
  <table><thead><tr><th>要素</th><th>影響</th></tr></thead><tbody>
    <tr><td>状態</td><td>傷や汚れがあると減額されやすい</td></tr>
    <tr><td>付属品</td><td>箱・説明書・特典があるとプラスに</td></tr>
    <tr><td>需要</td><td>人気作品や限定品は高値になりやすい</td></tr>
  </tbody></table>

  <h2>売る前の手順</h2>
  <ol>
    <li>売る商品をリストアップする</li>
    <li>状態を写真で記録する</li>
    <li>複数社で無料査定を比べる</li>
    <li>納得した業者に申し込む</li>
  </ol>

  <h2>まずは査定だけ</h2>
  <p>すぐに売らなくても、査定額を知っておくだけで判断がしやすくなります。A8.net経由なら買取成立で報酬が発生する案件もあります。</p>

  <h2>よくある質問</h2>
  <dl class="faq">
    <dt>査定は無料？</dt><dd>多くの買取サービスで無料査定が可能です。詳細は公式サイトをご確認ください。</dd>
    <dt>送料は誰が負担？</dt><dd>業者によって異なります。送料無料キャンペーンを行うサービスもあります。</dd>
  </dl>
""",
        "cta": JANI, "cta_text": "無料査定を申し込む →", "related": [("GMO光アクセスの比較", "gmo-hikari.html")],
    },
]

for a in ARTICLES:
    p = pathlib.Path(a["file"])
    p.write_text(build(a), encoding="utf-8")
    print("created", p)
