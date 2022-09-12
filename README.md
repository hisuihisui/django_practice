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
### shell_plusの使用
1. django_extensionsとptpythonのインストール
```
pip install django-extensions
pip install ptpython
```
2. settings.pyの編集<br>
下記をsettings.pyに追記
```
INSTALLED_APPS = (
    ...
    "django_extensions",
    ...
)

SHELL_PLUS = "ptpython"
```
3. shell_plusを起動
```
python manage.py shell_plus
```
### Userモデルの取得
```
from django.contrib.auth.models import User

# adminユーザの取得
user = User.objects.get(username="admin")
```
### QuerySetオブジェクト
queryプロパティを使用して、sqlを確認できる
```
# 例
print(Snippet.objects.filter(id__gte=1).query)
```
### select_related メソッド
ForeignKeyやOneToOneFieldのフィールドをINNER JOIN<br>
　→テーブル結合を行ってから取り出す<br>
　　→単一の値が紐づく関係のみに使用可能
### prefetch_related メソッド
1回目にあるテーブルの一覧を取り出し、そのIDをもとに結合先のテーブルの情報を取り出す
