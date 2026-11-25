import pathlib

SPEED = {
    "nuro": ("NURO光", "976 Mbps", "782 Mbps", "11.5 ms"),
    "au": ("auひかり", "706 Mbps", "622 Mbps", "16.3 ms"),
    "docomo": ("ドコモ光", "629 Mbps", "480 Mbps", "21.0 ms"),
    "softbank": ("ソフトバンク光", "580 Mbps", "471 Mbps", "17.1 ms"),
    "flets": ("フレッツ光ネクスト", "407 Mbps", "300 Mbps", "23.9 ms"),
    "gmo": ("GMOとくとくBB光", "630 Mbps", "526 Mbps", "19.2 ms"),
}

MAP = {
    "articles/docomo-hikari.html": ("docomo", "独自回線のNURO光・auひかりと比べると、下り・上り・Pingともに控えめです。ただし全国対応とドコモのセット割が魅力で、スマホをまとめたい人には向いています。"),
    "articles/gmo-access.html": ("gmo", "GMO光アクセス自体の実測データは公開が限られますが、同じGMOとくとくBBの光コラボ実績では下り630Mbps台。独自回線には及ばないものの、光コラボ内では上位です。"),
    "articles/softbank-hikari.html": ("softbank", "ソフトバンク光は下り580Mbps台。独自回線のNURO光（976Mbps）よりは遅いですが、ソフトバンク・ワイモバイルのセット割を考慮すると総合的に得なケースがあります。"),
    "articles/flets-hikari.html": ("flets", "フレッツ光ネクストは下り407Mbps台と、比較した中では最も控えめです。ただし光コラボ各社が利用する基盤そのもので、エリアと安定性に強みがあります。"),
    "articles/nuro-hikari.html": ("nuro", "独自回線の中でも突出して速く、上り・Pingも含めてトップクラス。ただし提供エリアが限られるため、まず自宅が対象かを確認しましょう。"),
    "articles/au-hikari.html": ("au", "独自回線として夜間の低下が少なく、上りも速いです。au・UQユーザーならセット割も含めて有力候補になります。"),
}

for name, (key, note) in MAP.items():
    p = pathlib.Path(name)
    s = p.read_text(encoding="utf-8")
    if "他社との実測比較" in s:
        print("skip", name)
        continue
    rows = ""
    for k in [key, "nuro", "au", "docomo"]:
        n, down, up, ping = SPEED[k]
        marker = "（この回線）" if k == key else ""
        rows += f"<tr><td>{n}{marker}</td><td>{down}</td><td>{up}</td><td>{ping}</td></tr>"
    block = f"""
  <h2>他社との実測比較</h2>
  <table>
    <thead><tr><th>回線</th><th>下り</th><th>上り</th><th>Ping</th></tr></thead>
    <tbody>
{rows}    </tbody>
  </table>
  <p class="cta-note">出典：みんなのネット回線速度（直近3か月平均）。環境により変動します。</p>
  <p>{note}</p>

  <h2>こんな人に向いている／向いていない</h2>
  <ul>
    <li><strong>向いている</strong>：{MAP.get(name)[1] if False else note.split("ただし")[0].rstrip("。")}</li>
    <li><strong>向いていない</strong>：とにかく最速の下り速度だけを求める人（独自回線の検討をおすすめします）</li>
  </ul>
"""
    s = s.replace("<h2>申し込み前に確認すること</h2>", block + "  <h2>申し込み前に確認すること</h2>", 1)
    p.write_text(s, encoding="utf-8")
    print("updated", name)
