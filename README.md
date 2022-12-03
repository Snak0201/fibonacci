# Fibonacci API
リクエストパラメータ`n`をつけてGETすることで、フィボナッチ数列の`n`番目の数値を返すAPIです。
フィボナッチ数列は次のような数列です。
      
      [1, 1, 2, 3, 5, 8, ...]

例:

GET `/fib?n=1`
      
      {"result": 1}

GET `/fib?n=4`
      
      {"result": 3}

# API
## GET `/fib?n={positive_number}`
リクエストパラメータの`positive_number`には、フィボナッチ数列の何番目を取得したいかを数字で入力します。数字の全半角は不問です。
`positive_number`には1以上の値が期待され、0以下の値はエラーとなります。また、数字以外の文字列や`n`の値を指定しない場合もエラーとなります。

リクエストパラメータ`n`が2つ以上指定されている場合は、最後の値が適用されます。`n`以外のパラメータは無視されます。

GET以外のリクエストは許可されず、エラーとなります。

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
