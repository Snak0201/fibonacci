# Fibonacci API
リクエストパラメータ`n`をつけてGETすることで、フィボナッチ数列の`n`番目の数値を返すAPIです。

# ディレクトリ構成
<pre>
│  .gitattributes
│  .gitignore
│  db.sqlite3
│  fibonacci.pyproj
│  fibonacci.pyproj.user
│  fibonacci.sln
│  manage.py
│  README.md
│  requirements.txt
│  
├─api
│  │  admin.py
│  │  apis.py           : APIの定義
│  │  apps.py
│  │  serializers.py    : APIのバリデーションの定義
│  │  tests.py          : APIのテスト
│  │  urls.py           : URLの設定ファイル
│  │  __init__.py
│  │  
│  └─migrations
│        __init__.py
│  
└─fibonacci
      settings.py : APIの設定ファイル
      urls.py     : URLの設定ファイル
      wsgi.py
      __init__.py
</pre>

# 要件
| ライブラリ名 | 概要 |
| ---- | ---- |
| django |  Webフレームワーク  |
| djangorestframework | djangoでREST APIを開発しやすくするライブラリ |

# API
## GET `/fib?n={positive_number}`
リクエストパラメータの`positive_number`には、フィボナッチ数列の何番目を取得したいかを半角数字で入力します。
