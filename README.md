# 年末ごちそうガイド（A8.net アフィリエイトブログ）

おせち・かにに特化した静的サイト。GitHub Pages で公開します。

**公開URL:** https://burattom.github.io/osechi-guide/
**リポジトリ:** https://github.com/Burattom/osechi-guide

## 構成

```
.
├── index.html                      トップ
├── articles/osechi.html            おせち比較記事（匠本舗）
├── articles/osechi-saitei.html     おせち早割（長尾キーワード）
├── articles/osechi-kaihou.html     おせち解凍（長尾キーワード）
├── articles/kani.html              かに比較記事（かに本舗）
├── articles/kani-ryo.html          かに内容量（長尾キーワード）
├── articles/kani-kaihou.html       かに解凍（長尾キーワード）
├── about.html                      アフィリエイト開示 / ポリシー
├── sns/instagram-posts.md          Instagram投稿文案（SNS用リンク）
├── tracking/report.md              効果測定ログ
├── style.css
└── .github/workflows/deploy.yml
```

記事内のCTAリンクは A8.net の広告リンクに差し替え済みです（`rel="nofollow sponsored"` 付き）。

| 記事 | 対象プログラム | プログラムID | 状態 |
|---|---|---|---|
| `articles/osechi.html` | 匠本舗 料亭おせち | `s00000009319002` | 提携完了・リンク反映済み |
| `articles/kani.html` | かに本舗 | `s00000009319001` | 提携完了・リンク反映済み |

A8.net にはサイトID `003`（年末ごちそうガイド）として登録済みです。

## 公開手順（GitHub Pages）

1. GitHub で新しいリポジトリを作成する（例: `osechi-guide`）。**Public** にすること。
2. このフォルダの中身をリポジトリのルートとして push する。

   ```powershell
   cd D:\ssdproject\A8-afiliate
   git init
   git add .
   git commit -m "initial commit"
   git remote add origin https://github.com/<あなたのユーザー名>/<リポジトリ名>.git
   git branch -M main
   git push -u origin main
   ```

3. リポジトリの **Settings → Pages → Build and deployment** で、Source を **GitHub Actions** にする。
4. Actions タブの「Deploy to GitHub Pages」が緑になったら公開完了。
   公開URLは `https://<ユーザー名>.github.io/<リポジトリ名>/` です。

> 既にリポジトリがある場合は `git init` は不要です。

## A8.net 側の手順（あなたが行う）

1. メディア管理画面 → **登録情報 → サイト情報の登録・修正** を開く
2. 再認証（ログインID / パスワード）を入力する
3. 新しいサイト情報を登録する
   - サイト名：`年末ごちそうガイド`
   - サイトURL：上記の公開URL
   - カテゴリ：グルメ・食品 など
4. **プログラム検索** で下記を探し、提携申請する（どちらも即時提携）
   - `s00000009319002`（匠本舗 おせち）
   - `s00000009319001`（かに本舗）
5. 提携後、**プログラム管理 → 参加中プログラム** から広告リンクを取得し、記事のプレースホルダーを差し替える
6. 公開後、**広告掲載URL管理** から記事URLを提出する（A8の規約で必須）

差し替え用リンクを私に渡してもらえれば、ファイルへの反映もします。

## 注意点

- 匠本舗 / かに本舗はリスティング広告のNGワードが多数あります。有料広告を出す場合は管理画面の「リスティングNGワード」を必ず確認してください。
- 成果確定目安は約30日です。
