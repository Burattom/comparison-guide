# 効果測定ログ

A8.net メディア管理画面 → レポート → 期間別（日別）／プログラム別（サマリ）の数値を記録する。

## 対象プログラム

| 略称 | プログラムID | 記事URL |
|---|---|---|
| おせち | s00000009319002 | https://burattom.github.io/osechi-guide/articles/osechi.html |
| おせち早割 | s00000009319002 | https://burattom.github.io/osechi-guide/articles/osechi-saitei.html |
| おせち解凍 | s00000009319002 | https://burattom.github.io/osechi-guide/articles/osechi-kaihou.html |
| かに | s00000009319001 | https://burattom.github.io/osechi-guide/articles/kani.html |
| かに内容量 | s00000009319001 | https://burattom.github.io/osechi-guide/articles/kani-ryo.html |
| かに解凍 | s00000009319001 | https://burattom.github.io/osechi-guide/articles/kani-kaihou.html |

## SNS用リンク（Instagram）

| 案件 | SNS・note用リンク |
|---|---|
| おせち | `https://px.a8.net/svt/ejp?a8mat=4BGTLG+1UOLAY+1ZWM+BZO4I&a8sns=instagram` |
| かに | `https://px.a8.net/svt/ejp?a8mat=4BGTLG+1WGW4A+1ZWM+60H7M&a8sns=instagram` |

SNS投稿文は `sns/instagram-posts.md` を参照。PR表記・公開アカウント必須。

## 投稿済み

| 日付 | 投稿 | URL |
|---|---|---|
| 2026-11-25 | おせち早割（低解像度版・削除済み） | https://www.instagram.com/p/DgIfPIvyvdb/ |
| 2026-11-25 | おせち早割（1080x1080再投稿） | https://www.instagram.com/p/DgJVGAVyS2q/ |

公開投稿URLは両プログラムの「広告掲載URL管理」に提出済み。

@ririachannnn のプロフィール「ウェブサイト」に `https://burattom.github.io/osechi-guide/` を設定済み（2026-11-25 確認）。Instagramが `utm_source=ig` を付与するため、流入元を判別可能。

## GA4

- 測定ID `G-FVZHH3RMRT` を全ページに実装済み（2026-11-25）
- イベント：page_view / scroll / click（拡張計測）＋ A8リンクの離脱クリック
- 自分のBraveはトラッキングをブロックする可能性があるため、リアルタイム検証は別ブラウザで行うこと

## 日次記録

| 日付 | インプレッション | クリック | 発生件数 | 発生金額 | CVR | メモ |
|---|---|---|---|---|---|---|
| 2026-11-25 | 0 | 0 | 0 | 0円 | - | 公開初日。URL提出済み、インデックス待ち |
| 2026-11-25（再認証後） | 0 | 0 | 0 | 0円 | - | 未インデックスが原因と判明。Search Consoleで所有権確認・全7URLのインデックス登録をリクエスト済み |

## 改善アクションの判断目安

| 状態 | 考えられる原因 | 次の一手 |
|---|---|---|
| インプレッションが少ない | Googleに未インデックス／検索順位が低い | Search Consoleでインデックス確認、長尾キーワード記事を追加 |
| インプレッションはあるがクリックが少ない | タイトル／ディスクリプションが弱い | タイトルに「早割」「比較」「失敗しない」を入れる |
| クリックはあるが発生しない | LPとのミスマッチ／成果条件が重い | CTAの訴求を変える、無料登録系案件を並べる |
| 発生するが確定しない | キャンセル／条件未達 | 否認条件を読み直し、記事の表現を修正 |

## チェックする画面

- 簡易レポート（ホーム）：https://media-console.a8.net/home
- 期間別（日別）：https://media-console.a8.net/report/period/daily
- プログラム別（サマリ）：https://media-console.a8.net/report/program/summary
