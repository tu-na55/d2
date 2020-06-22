
#### init, lint
+ エラーコードのチートシート
ttps://qiita.com/KuruwiC/items/8e12704e338e532eb34a


pipenv graph | grep pytest

+ extention: Python

◎環境
ipython: 対話補完
sphinx: document生成


◎graph
pipenv install numpy pandas
matplotlib
seaborn


```py
[dev-packages]
ipython = "*"
mixer = "*"
pytest-django = "*"
django-extensions = "*"

[packages]
django = "==2.0.5"
django-configurations = "*"
django-extensions = "*"
dj-database-url = "*"
mysqlclient = "*"
djangorestframework = "*"
djoser = "*"
django-cors-headers = "*"
```

◎pytest

pipenv install --dev pytest pytest-cov pytest-django
・pytest-cov	カバレッジ
・pytest-html	結果をHTML形式で出力
・pytest-datadir	テスト用ファイルを管理する
・pytest-dbfixtures	MySQL等の主要なDBの fixture
より複雑なモックには標準ライブラリの unittest.mock を使います。

◎linter, formatter
pipenv install --dev flake8 mypy
pipenv install black
<!-- pep8 -->
flake8: pycodestyle, pyflakes, mccabeの3つのLinterを統一的に扱うwrapper
<!-- flake8-import-order -->
<!-- flake8-docstrings -->
<!-- autopep8 -->


◎django
django djangorestframework django-filter django-cors-headers

以下未確認
django-extensions = "*"
django-configurations = "*"

◎認証
djoser djangorestframework_simplejwt
<!-- djangorestframework-jwt -->


◎DB
mysqlclient: driver
psycopg2: postgre driver

sqlalchemy: ORM。DBはSQLiteで構築し、ORMモジュールであるSQLAlchemyを使ってデータを操作します。

records: get？


◎データ取得
requests beautifulsoup4
importlib: reload

◎画像処理
opencv-python pillow

◎機械学習
torch torchvision

___

・drf-yasg(Swagger): API実装したはいいけど、ドキュメント作るのは面倒くさいし、動作確認するのにPostmanやcurlを使うのも面倒くさい、というときに便利なのがSwagger UIです。

・fastapi graphene uvicorn : FastAPI + graphQL




#### init
C:\Users\[usr]\AppData\Local\Programs\Python\Python38
C:/Users/[usr]/AppData/Local/Programs/Python/Python38

Win: 公式からexecutable版をインストール
環境変数参考
C:\Users\[usr]\AppData\Local\Programs\Python\Python38\Scripts\
C:\Users\[usr]\AppData\Local\Programs\Python\Python38\
C:\Users\[usr]\AppData\Local\Programs\Python\Launcher\

pipenv
@win: システム変数
PIPENV_VENV_IN_PROJECT=1
<!-- PIPENV_IGNORE_VIRTUALENVS=1 -->
<!-- PIPENV_VERBOSITY=-1 -->

次のうちの二択
#01 仮想環境の親ディレクトリ指定してインストール
$ export WORKON_HOME=~/.venvs
$ pipenv install 

#02 プロジェクト直下
$ export PIPENV_VENV_IN_PROJECT=1
$ pipenv install 



@VScode
python
python extention pack
python docstring

devcontainer.json
{
    "name": "Python3_Pipenv",
    "dockerFile": "Dockerfile",
    "appPort": 9000,
    "context": "..",
    "extensions": [
        "ms-python.python"
    ],
    "settings": {
        "python.pythonPath": "/usr/local/bin/python"
    }
}


```bash
___
####################
### windows, Ver3.8.1
# => .dll一式をenv/Scriptsにコピーしておく。
# prj pyenv.cfg
# Scripts(win): bin(unix)

# Scripts配下にライブラリがインストールされる。
# home = Scripts
####################

####################
# win, ver3.8.3
# appフォルダ以下の旧バージョンを削除、再インストールしたら解決
# インストーラ経由でupgradeしたら、問題が起きなかったかもしれない。
####################
```


```bash
◎親環境、仮想環境ともにpip, setuptoolsをupgrade
python -m pip list --outdated
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
# python -m pip install -U pip

# 強制アップグレード。
python -m pip install --upgrade --force-reinstall pip

--proxy="http://user:password@domain.com"
# '@': '%40'
####################
◎実際に使うのは、ほぼpipenvのみ: pip, venvのラッパー
◎MacやLinuxならpyenv, direnvも併用。

アプリケーション: 直接使うことができるもの。
ライブラリ: 他のライブラリやアプリケーションに組み込まれて使うもの

◎setup.cfgのinstall_requires
app: 指定なし
lib: 依存パッケージを書く。ゆるいバージョン指定。

◎Pipfile/Pipfile.lock 
app: 本番環境用の依存パッケージと、開発用の依存パッケージの両方を指定する（本番は[packages] に、開発は[dev-packages]に書く）
lib: 開発用の依存パッケージだけを指定

◎要するに、appは同じ環境を本番環境に書く。

####################
python -m pip install pipenv

# vs-codeの設定で自動化されてるけど、本来はavtivateしてから。
source .venv/Scripts/activate
# deactivate
# cd .venv/Scripts/ && deactivate

echo $VIRTUAL_ENV
pipenv install --python 3
pipenv --venv
# 仮想環境削除
# pipenv --rm

# pipfile.lockからの導入
# pipenv install

pipenv update --outdated
pipenv update
pipenv check

# Pipfile を元に Pipfile.lock を最新に更新するが、インストールしない。
# pipenv lock

他のマシン上で同じ環境を再現するには、リポジトリを clone した上で
pipenv sync を実行する。

pipenv lock --clear
####################
# 仮想環境に入る
pipenv shell

# which pythonは使わない？
pipenv run python --version
pipenv run python test_about.py

# installed packagge-list
pipenv graph

pipenv install numpy pandas
pipenv install --dev flake8 black mypy
# pipenv install --skip-lock [pkg]



####################
# # venv + pip時代
# python -m django --version
# # license, location
# python -m pip show [package]

# mkdir prj && cd prj
# python -m venv [venv]
# cd C:/Users/[user]/OneDrive/デスクトップ/ws/nuxt/d
# # source venv/Scripts/activate
# # source venv/Scripts/deactivate
# # 下記じゃないと無効化できなかった。
# # deactivate

# source .venv/Scripts/activate
# cd .venv/Scripts/ && deactivate

# ### @mac ###
# # source venv/bin/activate

# # venv/Scripts/python --version
# # venv/Scripts/python test.pyw

# # project用にinstall, uninstall
# # activateしてから実行。親環境にはインストールしないこと。
# python -m pip freeze > requirements.txt

# # 以下を追記
# flake8
# black

# # バージョン固定
# Flask ~= 0.12.2
# # メジャーバージョンだけ固定
# Flask == 0.*

# python -m pip install -r requirements.txt

# # CI環境と本番環境では固定された、再現性のあるバージョンで実行したいとき、.lockに出力。
# pip freeze > requirements.lock
# pip install -r requirements.lock

# # プロジェクト以外も含めてバージョン統一。
# # constraints.txtは基本的には使わなくていい。
# # requirements.txtに記載されてる場合は、constraints.txtのverで固定。
# # なければ、インストールされない。
# pip install -r requirements.txt -c constraints.txt

####################

```


##### package
```bash
# prepare setup.cfg, setup.py

# version text
pip freeze > constraints.txt
# usage
pip install -e . -c constraints.txt


# ローカルでインストール(開発モード)
# これで、ローカル環境ではどこからでもインポートできる。
pip install -e
python setup.py develop
```


```bash
CountDownApp
├── CountDownApp       # パッケージの中身
│   ├── __init__,py 
│   └── app.py        
├── MANIFEST.in        # 配布ソースコードに何を含めるか書いたファイル
├── README.rst         # 長い説明とかをまとめているファイル
├── VERSION            # 勝手に作ったバージョンファイル
├── image.png          # ただの画像
├── requirements.txt   # 依存している他のパッケージをまとめるやつ
├── setup.cfg          # オプションをまとめる便利なファイル
└── setup.py           # パッケージの情報が詰まったファイル
```

```bash
# 配布用ソースコードの作成
python setup.py sdist

# MANIFEST.in に従ってパッケージ化される。
# MANIFEST.in
include README.rst
include setup.cfg

# 配布用のバイナリの作成
# wheel パッケージを利用するのでインストールしておく。
pip install wheel
# 実行方法は
python setup.py bdist_wheel


Defining the Python versionでは、
--universal と --python-tag XXX が説明されてあるが、どの環境に対してパッケージ化するかが選択できる。

setup.cfg ファイルにこれらのオプションをまとめておくことができる。

[bdist_wheel]
universal=1
こうすれば、わざわざオプションをつけなくてよい。

# PyPIへアップロード
# 配布用のソースコードとバイナリを作成してアップロードするなら
python setup.py sdist bdist_wheel upload
```


___





#### django


```bash
#02
django-admin startproject config .
親のconfigフォルダ削除

python manage.py startapp app
# config.setting.py: add 'app'
# create app.urls.py
# app.views.py
python manage.py runserver
# http://127.0.0.1:8000/

# モデルを作成し構造を定義したため、マイグレーション用のファイルを作成しモデルの変更をデータベースに反映させる必要があります。
python manage.py makemigrations
# No changes detectedが出たら、app名を指定する。
# python manage.py makemigrations core
python manage.py migrate

# app.adimin
# 管理画面にアクセスするためのスーパーユーザを作成
python manage.py createsuperuser
python manage.py runserver

####################
# JWT認証
# トークンの発行
USERNAME='admin'
PASSWORD='userpassword'

curl http://127.0.0.1:8000/api-auth/ -d "username=${USERNAME}&password=${PASSWORD}"

# トークンありでGETリクエスト
JWT=$(curl -s -XPOST http://127.0.0.1:8000/api-auth/ -d "username=${USERNAME}&password=${PASSWORD}" | jq -r .token)
curl -XGET -H "Authorization: JWT ${JWT}" http://127.0.0.1:8000/api/memo/

# POSTしてデータ登録
curl -XPOST -H "Authorization: JWT ${JWT}" http://127.0.0.1:8000/api/memo/ -d 'title=title_2&memo=use_jwt'
curl -XGET -H "Authorization: JWT ${JWT}" http://127.0.0.1:8000/api/memo/

# 02 simple_jwt
認証されていないので値を取得できません。
curl http://127.0.0.1:8000/api/sublist/ | jq .

curl http://127.0.0.1:8000/api/auth/jwt/create -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"username":"${USERNAME}","password":"${PASSWORD}"}'

curl http://127.0.0.1:8000/api/sublist/ -H 'Authorization: JWT [トークンを入力]' | jq .




```


```bash
# prj-init, config(parent): prjName
django-admin startproject config .
# rename prjName
mv config prj && cd prj

# db-init
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/

# python manage.py runserver 127.0.0.1:8080
# http://127.0.0.1:8080/
####################
# setting.py => ['127.0.0.1']

admin.py, models編集、ログイン、テーブル作成。

# アプリの作成
python manage.py startapp app
# settinng.py, add myApp


# dbに反映, model定義のテーブル
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate

# python manage.py makemigrations --empty --name customers customers

# admin@test_test
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin/


### download: command-line shell program
# python manage.py dbshell
###

### Test_ParamABC
# from app.models import Test_ParamABC
# for params in (
#     {'a': 'a', 'b': 0, 'c': True},
#     {'a': 'b', 'b': 1, 'c': False},
#     {'a': 'c', 'b': 2, 'c': True},
# ):
# Test.objects.create(**params)
###
models.py
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
  status = models.CharField(default='Unstarted', max_length=100)

serializers.py
  fields = (
      'id',
      'title',
      'description',
      'status',
  )

# 追加
curl -X POST -H 'Content-Type:application/json' -d '{"title":"t_2","description":"d_2"}' http://localhost:8000/todos/

# 取得
curl -X GET http://localhost:8000/todos/2/
curl -X GET http://localhost:8000/todos/2.json
curl http://localhost:8000/books

# 書き換え
curl -X PUT -H 'Content-Type:application/json' -d '{"title":"t2","description":"d2_p"}' http://localhost:8000/todos/2/

# 削除
curl -X DELETE http://localhost:8000/todos/3/
####################


全てのアプリケーションにある静的ファイルを自動で一箇所に集めてくれます。
python manage.py collectstatic


####################
setting.pyにrest_frameworkを追加
error_handler用のutil.py作成

# urlルート
config/urls => todos/urls => views

# serializers.py：dateをJSONに変換
models table => selializers meta-fields => views get/put => todos/urls



# setting.py
'myApp.apps.MyappConfig',

python manage.py startapp polls
作成されたアプリのviewを編集する
https://docs.djangoproject.com/ja/2.1/intro/tutorial01/を確認

URLconfを編集
https://docs.djangoproject.com/ja/2.1/intro/tutorial01/を確認

サーバー起動し、ブラウザで確認

python manage.py runserver
http://localhost:8000/polls/にアクセスして確認
```

___
