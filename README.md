# 実践Django Pythonによる本格Webアプリケーション開発
https://www.amazon.co.jp/gp/product/B095BZPJYW/ref=ppx_yo_dt_b_d_asin_title_o07?ie=UTF8&psc=1

## スニペットへのコメント機能
1. モデルの作成
2. ビュー
    GETとPOSTで処理分ける
    リダイレクトで同じ画面に飛ばす
3. テンプレート
    formをたす
<br><br>
残タスク<br>
    コメント一覧の見た目を整える

## 2. モデル定義とクエリ操作
### マイグレーションファイル→SQLの確認
```
python manage.py sqlmigrate <app_name> <migration_name>
```
