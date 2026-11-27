# 効果測定ログ

A8.net メディア管理画面 → レポート → 期間別（日別）の数値を記録する。

## 対象プログラム

| 略称 | プログラムID | 記事URL |
|---|---|---|
| ドコモ光 | s00000000018031 | https://burattom.github.io/comparison-guide/articles/docomo-hikari.html |
| GMO光アクセス | s00000000018040 | https://burattom.github.io/comparison-guide/articles/gmo-hikari.html |
| ジャニキング | s00000016322002 | https://burattom.github.io/comparison-guide/articles/goods-buyback.html |

## 日次記録

| 日付 | インプレッション | クリック | 発生件数 | 発生金額 | CVR | メモ |
|---|---|---|---|---|---|---|
| 2026-11-25 | 0 | 0 | 0 | 0円 | - | 通年案件へピボット。季節記事・IG投稿は削除済み |
| 2026-11-26 | 0 | 6 | 0 | 0円 | - | 再認証後に取得。クリック6件は6案件それぞれ1件ずつ＝設定時にリンク確認したテストクリック。実流入はまだ0 |

## その他の計測（2026-11-26 時点）

### GA4（過去7日間）
- アクティブユーザー：5／表示回数：16／イベント数：35
- 国：United States 3／Japan 1（＝ほぼ当方の検証アクセスと推定）
- ページ：比較ガイド13回／旧タイトル3回

### Search Console
- 検索パフォーマンスは「データを処理しています。1日後にもう一度」のまま
- 検索クリック・表示回数はまだ0

### Instagram（@ririachannnn）
- フォロワー0／フォロー中0／投稿1件
- 投稿インサイト：ビュー0／いいね0／コメント0／保存0／シェア0／プロフアクセス0／外部リンクタップ0
- 教育投稿を公開したが、まだリーチゼロ

#### 教育投稿（2026-11-27 公開）
- 投稿URL：https://www.instagram.com/p/DgOgT7yy_sf/
- 画像：`edu-tennyou-1080.png`（1080x1080、光回線の乗り換え3種類の図解）
- キャプション：転用／事業者変更／新規開通の3types解説（広告リンクなし、プロフィールリンクへ誘導）
- 投稿直後のため、インサイト数値は未反映（後日確認）

### 外部露出（2026-11-26 時点）
- **Microsoft アカウント**：`amatu.riria@gmail.com` で作成完了（長押し認証はユーザーが実施）
- **Bing Webmaster Tools**：ユーザーが手動サインイン後、以下完了
  - サイト `https://burattom.github.io/comparison-guide/` を手動追加（GSCインポートは「サイトが見つかりません」で失敗）
  - `index.html` に `<meta name="msvalidate.01" content="6264854A119B84CC92DB50E584993472">` を追加して確認済み
  - `sitemap.xml` を送信（状態：処理中）
  - 主要11URLを直接送信（トップ＋全9ページ、1件は誤URLのため再送信済み／残クォータ89）
- **はてなブログ**：https://hikari-hikaku.hatenablog.com/ を開設（無料プラン、公開範囲：すべての人に公開）
- **はてな転載記事**：https://hikari-hikaku.hatenablog.com/entry/2026/11/26/123450 を公開（元記事へのリンク明記、テーブル含む本文1,060文字）
- **note**：https://note.com/hikari_hikaku/n/n43025a9bc290 を公開（本文1,277文字、ハッシュタグ #光回線 / #光回線乗り換え、元記事リンク明記）。未ログインでも閲覧可を確認
- **X**：@hikarihikaku を作成（ユーザーがSMS認証を完了）。表示名・bio・サイトリンクを設定し、`sns/x-posts.md` の投稿5件を公開済み
- **A8.net サイト登録**：サイトID 003 を更新（再認証後）。`年末ごちそうガイド` / `https://burattom.github.io/osechi-guide/` → `光回線・グッズ買取の比較ガイド` / `https://burattom.github.io/comparison-guide/`、カテゴリ「インターネットサービス」に変更

## 改善アクションの判断目安

| 状態 | 考えられる原因 | 次の一手 |
|---|---|---|
| インプレッションが少ない | 未インデックス／順位が低い | Search Consoleでインデックス確認、長尾キーワード記事を追加 |
| インプレッションはあるがクリックが少ない | タイトル／説明が弱い | タイトルに「比較」「失敗しない」を入れる |
| クリックはあるが発生しない | LPとのミスマッチ／成果条件が重い | CTAの訴求を変える、他案件を並べる |
| 発生するが確定しない | キャンセル／条件未達 | 否認条件を読み直し、記事の表現を修正 |

## チェックする画面

- 期間別（日別）：https://media-console.a8.net/report/period/daily
- プログラム別（サマリ）：https://media-console.a8.net/report/program/summary
- GA4：測定ID `G-FVZHH3RMRT`
