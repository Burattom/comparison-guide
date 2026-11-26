# 比較ガイド（A8.net アフィリエイトブログ）

光回線の乗り換え・グッズ買取に特化した静的サイト。GitHub Pages で公開。

**公開URL:** https://burattom.github.io/comparison-guide/
**リポジトリ:** https://github.com/Burattom/comparison-guide
**sitemap:** https://burattom.github.io/comparison-guide/sitemap.xml

> 2026-11-25：季節案件（おせち・かに）は撤収し、通年案件へピボットしました。
> Instagramの投稿・予約もすべて削除済み。
> 2026-11-26：A8.net サイトID 003 の登録URLを `https://burattom.github.io/comparison-guide/` に更新済み（旧：`osechi-guide`）。

## 構成

```
.
├── index.html                        トップ
├── articles/docomo-hikari.html       ドコモ光の乗り換え
├── articles/gmo-hikari.html          光回線比較（GMO光アクセス）
├── articles/goods-buyback.html       グッズ買取の比較
├── about.html                        アフィリエイト開示 / ポリシー
├── tracking/report.md                効果測定ログ
├── style.css
└── .github/workflows/deploy.yml
```

## 稼働中の案件（即時提携）

| 案件 | プログラムID | 報酬 |
|---|---|---|
| GMOとくとくBB ドコモ光 | s00000000018031 | 9,000〜17,000円 |
| GMO光アクセス | s00000000018040 | 6,000円 |
| ジャニーズグッズ買取【ジャニキング】 | s00000016322002 | 買取成立2,500円 |
| SoftBank光（NEXT） | s00000014546008 | 新規10,000円／転用7,500円 |
| GMOとくとくBB ソフトバンク光 | s00000000018043 | 新規開通＋利用12,000円 |
| フレッツ光申込窓口 | s00000007633011 | 新規開通20,000円 |

## 審査中の案件

承認後に広告リンクを取得し、記事を追加予定。

| 案件 | プログラムID | 報酬 |
|---|---|---|
| 保育士人材バンク | s00000001248025 | 初回登録5,000円 |
| PT・OT・ST WORKER | s00000026401001 | 新規会員登録3,790円 |
| 街角雨漏り相談所 | s00000024877004 | 新規見積7,000円 |

## SEO / 計測

- canonical / OGP / Twitter Card を全ページに設定
- Article / FAQPage / BreadcrumbList のJSON-LD
- sitemap.xml / robots.txt を設置、全記事のインデックスをリクエスト済み
- CTAを冒頭・中段・末尾の3箇所に配置
- Lighthouse: Accessibility 1.00 / Best Practices 1.00 / SEO 1.00
- Google Search Console：所有権確認済み
- GA4：測定ID `G-FVZHH3RMRT`（プロパティ名：比較ガイド）

## Instagram

- アカウント：@ririachannnn（**ビジネスアカウント**／カテゴリ：個人ブログ）
- 表示名：りりあ｜光回線・買取の比較ガイド
- 自己紹介：
  ```
  光回線の乗り換え・グッズ買取を比較💡
  工事費／キャッシュバック／査定額の確認ポイントを解説
  A8.net提携メディアの比較ガイド
  記事はプロフィールリンクから👇
  ```
- プロフィールリンク：`https://burattom.github.io/comparison-guide/`
- 投稿：教育シリーズを運用中（初回：https://www.instagram.com/p/DgKNVknSUR7/）
- アイコン：`sns/assets/profile-icon.png`（`scripts/make_profile_icon.py` で生成）
- 教育投稿画像：`sns/assets/edu-*.png`（`scripts/make_edu_posts.py` で生成）
- 運用方針：`sns/growth-plan.md`

## 外部メディア

- **はてなブログ**：https://hikari-hikaku.hatenablog.com/ （ID：`hikari-hikaku`／PW：`Hikari2026!Hatena#9Q`）
  - 転載記事：https://hikari-hikaku.hatenablog.com/entry/2026/11/26/123450
  - 原稿：`sns/crosspost-note.md`（元記事リンク明記済み）
- **note**：ID `hikari_hikaku`／PW `Hikari2026!Note#7Kp`
  - 公開記事：https://note.com/hikari_hikaku/n/n43025a9bc290 （#光回線 / #光回線乗り換え）
  - 原稿：`sns/crosspost-note.md`
- **Bing Webmaster Tools**：`amatu.riria@gmail.com` でサインイン済み。サイト確認済み（`index.html` の `msvalidate.01` メタタグ）／`sitemap.xml` 送信済み／主要URL送信済み
- **X**：@hikarihikaku（表示名：光回線・買取の比較ガイド／プロフリンク：比較ガイドTOP）
  - 投稿5件を公開済み（自己紹介・独自回線vs光コラボ・実測速度・工事費・グッズ買取）
  - 投稿案：`sns/x-posts.md`

## 回線別画像

各回線のヒーロー／サムネイルは`assets/{回線}-hero.jpg` / `{回線}-thumb.jpg`に個別設定済み。

- 出典：A8.netが配布する広告主公式バナーをネット経由で取得（`scripts/fetch_banners.py` / `fetch_more_banners.py`）
- 生成：`scripts/make_provider_images.py` で公式バナー＋回線名・種別を合成
- NURO光／auひかりはA8案件がないため、**各社公式サイトで公開されている画像**を取得して使用（`scripts/fetch_official_images.py` / `make_official_images.py`）
  - NURO光：公式サイトのキービジュアル（2,880×1,620）
  - auひかり：au公式「auひかりプラス」キャンペーンバナー（640×640）
- 元バナー：`assets/provider-*.jpg` / `gmo-banner.jpg` / `jani-banner.jpg` / `official-*.jpg`
- ※ 公式画像は各社の著作物です。紹介・比較目的での利用にとどめ、権利者からの要請があれば差し替えます
