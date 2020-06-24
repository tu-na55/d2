 CHANGELOG.md
「エンタープライズアーキテクチャ」
「業務システム モデリング」

___
Mock: Figma, ProtoPie
create gif: ScreenFlow, LICEcap, Principle, and After Effects.
<!-- Create GIFs with Sketch - Timeline plugin -->

AfterEfects Render
PS 800x600 Composition > Render Video
GIF Brewery 3 for Mac > 64 - 128 colors
ImageOptim for Mac (makes a .gif around 30% smaller)

splash movies
アニメーションスプラッシュ画面を作成するのは比較的簡単です。準拠した.mp4ファイルを作成し、このムービーの最初のフレームを起動イメージとして使用する必要があります。アプリの起動時にMPMoviePlayerControllerをインスタンス化して、ムービーをフルスクリーンで再生します。起動イメージが表示されてから数分後にムービーが再生されます。

起動イメージは静的ですが、xcodeで設定したイメージは変更できません。

しかし、スプラッシュ画面では、好きなようにすることができます。アニメーション、ビデオ、またはその他のものを表示するのはviewControllerです。 起動画像の後で「着陸ページ」の前にスプラッシュ画面を表示します。 次に、スプ​​ラッシュ画面で、フレームごとにアニメーションフレームを作成するか、MPMoviePlayerControllerに.mp4ビデオをロードすることができます。

アニメーションスプラッシュ画面を使用している人は、通常、スプラッシュ画面の色（最初のアニメーションフレームの色またはビデオの色）を使用して起動イメージを使用するため、起動イメージはスプラッシュ画面の一部です。
___
◎bashコマンド

```bash
jq => 
echo '{"foo": 0}' | jq .
type sample.json  | jq-win64.exe ".[]"
type sample.json  | jq-win64.exe ".[] | .aa"

@win
公式ダウンロード: jq-win64.exe
Git/usr/bin
今の環境だとエイリアス登録しなくても使えた。

@mac
sudo curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && sudo chmod +x /usr/bin/jq
```
___


github pages: gh-pages --save-dev:
contentful-cli: ヘッドレスCMS

アプリクライアント： Flutter( + Swift)( + Kotlin)


### Version 1.0
+ details


___


### over view

db -> port: 3306
nuxt -> port:3000
django -> port: 8000
nginx -> port:80 
  /admin,api,static -> proxy to django
  / -> proxy to nuxt


```bash
home
|- backend
| |- core（Djangoのプロジェクトが入る）
| |- config: app（APIを作成）
| |- Dockerfile
| |- requirements.txt
|- front
| |- nuxt （フロントのプロジェクト）
| |- Dockerfile
|- .gitignore
|- docker-compose.yml
|- README.md
```

```bash
├── docker-compose.yml        
├── mysite                   ← Djangoプロジェクトのルート
│   ├── Dockerfile             チュートリアルアプリであるpollsアプリを作成
│   ├── docker-entrypoint.sh
│   └── mysite
│       ├── manage.py
│       ├── mysite
│       ├── polls
│       └── static
├── mysql                    ← MySQLプロジェクトのルート
│   └── Dockerfile             mysql:5.7イメージを使うだけ
└── nginx                    ← Nginxプロジェクトのルート
    ├── Dockerfile             基本的にはnginx:1.15.alpineを使うだけだが、
    ├── docker-entrypoint.sh   Djangoと連携するためのUWSGI接続設定を組み込む
    └── mysite_nginx.conf
```

```bash
├─django
│  ├─manage.py
│  ├─composeexample
│  │   ├─settings.py
│  │   ├─urls.py
│  │   ├─wsgi.py
│  │   └─__init__.py
│  └─myapp
│      ├─migrations
│      ├─admin.py
│      ├─apps.py
│      ├─models.py
│      ├─renderers.py
│      ├─serializers.py
│      ├─tests.py
│      ├─urls.py
│      ├─views.py
│      └─__init__.py
│
├─docker-compose.yml
│
├─dockerfiles
│  ├─django_docker
│  │   ├─dockerfile
│  │   └─requirements.txt
│  └─nuxt_docker
│      └─dockerfile
│
├─mysql
│  └─conf.d
│
└─nuxt
    └─front
       └─以下略
```


```bash
├── README.md
├── batch
├── deploy
├── docker
│   ├── docker-compose.yml
│   ├── log
│   │   ├── nginx
│   │   │   ├── access.log
│   │   │   └── error.log
│   │   └── python
│   │       ├── error.log
│   │       └── request.log
│   ├── mysql
│   │   └── conf.d
│   │       └── custom.cnf
│   ├── nginx
│   │   ├── conf.d
│   │   │   ├── 00-log.conf
│   │   │   └── api.conf
│   │   └── nginx.conf
│   └── python
│       ├── Dockerfile
│       ├── startup.sh
│       └── uwsgi
│           └── api.ini
├── pip.list
├── venv
└── django

```

```bash
django
├── docker-compose.yml
├── mysql
│   ├── Dockerfile
│   └── init.d
│       └── init.sql
├── nginx
│   ├── conf
│   │   └── app_nginx.conf
│   └── uwsgi_params
└── python
    ├── Dockerfile
    └── requirements.txt

```



##### git

```bash
git init
git add .
# git add -A .
git commit -m "commit1"
# git commit -am "commit1"
git remote add origin https://github.com/[usr]/[repo].git
(git remote -v)
git push -u origin master
##########

git checkout -b test1
(git branch)

# ローカル最新化
git pull
# git pull origin master
# git fetch origin
git push origin test1
# githubでpull requestしてmerge。リモートbranchを削除

# ローカル最新化・ローカルbranch削除
git checkout master
git pull
git branch -D test1


# 上書き
git commit --amend
git revert [hashValue]
git rebase -i master

# 退避
git stash
(git stash list)
(git stash show -p stash@{1})
git checkout ハッシュ
# コンフリクトした
# git stash apply stash@{0}
git stash drop stash@{0}
b226224

git reset
git fetch

# 既存ファイルとの比較
git diff config/urls.py
```


・nginx + uWSGI
プロダクト利用では、Apache＋mod_python、または、Nginx＋uWSGI で動作させることが多い
```bash
80番ポート番号が解放されていない場合は、例えば下記の様にして開放する必要があります。
yum -y install firewalld
systemctl enable firewalld
systemctl start firewalld
firewall-cmd --add-port 80/tcp --permanent
firewall-cmd --reload
```


```bash
# ポートの使用状況
lsof -i:80


netstat -nap
netstat -na | grep ":80"
# 占領箇所を特定したら、そのプロセスをkillする
sudo kill 80


```

```bash
# 参考
・command: bash -c '複数行コマンド'  
# 一行にまとめるコマンド
・usermod -o -u 1000 mysql;
・groupmod -o -g 500 mysql;
・chown -R mysql:root /var/run/mysqld/;
・/entrypoint.sh mysqld --user=mysql --console'
```


##### Docker
docker-compose run python django-admin.py startproject mysite .

```bash
# まずはDockerfileだけで動かしてみる
docker build . -t pipenv_sample
docker run -it pipenv_sample
```

```bash
wsl_update_x64.msi
Docker Desktop Installer.exe

# 01
git clone [url].git
cd getting-started
docker build -t  [repo] .
docker run -d -p 80:80 --name [docker-tutorial] [repo]
docker tag [docker-tutorial] [docker-hub-account/repo]

# 02
docker-compose build #Dockerfileの環境を立ち上げる
docker-compose up -d #起動 -dはバックグラウンド。
docker exec -it backend bash #containerの中に入る

# 03
docker-compose up
docker ps

docker exec -it [containerName] bash

# version
docker-compose exec db mysql -V
####################
# 動作確認するため、一度コンテナを削除します。
docker-compose stop
docker-compose rm
# 検証用のDBなので、永続データも削除してしまいます。
rm -fr .data/
docker-compose up -d
####################
# コンテナと名前付きボリュームの削除が行えます。
$ docker-compose down --volumes
$ docker-compose up -d
####################
# ボリュームリスト
docker volume ls
# 使用していないボリュームの索条
docker volume prune
####################
sudo docker-compose run python django-admin.py startproject backend .

```

#### mysql

```sql
-- # ref: apache server
-- # sudo apachectl start
-- # mysql.server start

docker exec -it mysql bash
-- # use .env
docker-compose exec db bash -c 'mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE}'
-- # login_user
-- mysql -uroot -p
-- mysql -uroot -p -h 127.0.0.1 --port 13306
-- (ubuntu) mysql -h 127.0.0.1 -P 9999 -u root -D mysql -p 
mysql -u [user] -p
> [userPassword]
-- # ユーザ名確認
select user(), current_user();
-- # ログインユーザ権限確認
show grants for currtent_user();

CREATE DATABASE sample;
show databases;
use [dbName];
-- # 現在のDB
select database();

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255)
);

-- 末尾"\G"で見やすく表示
show tables\G
show table status where name='[table]';
show table status like 'u%'\G
select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='[mydb]' and TABLE_NAME='[table]'\G

-- collationでの曖昧検索
select * from [member] where [name] collate utf8_unicode_ci like '%keyword%';
-- ####################
-- # root user
-- # mysql -u root -e 'query';

-- # mysqlカラム一覧
SHOW COLUMNS FROM mysql.user;

CREATE USER 'mytest'@'localhost' IDENTIFIED BY 'Oracle2019%';
-- ユーザー一覧を表示する
SELECT Host, User FROM mysql.user;
SELECT Host, User, authentication_string FROM mysql.user;

-- ####################
-- 認証方式確認
SELECT user, host, plugin FROM mysql.user;
-- 認証方式変更
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'new_root_password';

-- 文字コード
show variables like '%char%';
-- ####################
-- # 権限確認
SHOW GRANTS FOR [user];
show grants for mytest@localhost;

-- ####################
-- 初期化
-- 5.6: mysql_install_db
-- 5.7: mysqld  --initialize


mysqld  --initialize  --console
-- ログ2行目に root のデフォルト・パスワードが出力されるので、必ず控えておくこと。この手順を怠ると初回ログインすらできなくなるので要注意です。

-- mysql起動
C:\mysql>bin\mysqld --console

-- # 初期化後の余計な権限削除の流れ
delete from mysql.user;
delete from mysql.db;
grant all on *.* to root@localhost with grant option;
flush privileges;

-- mysql8.0以降の流れ
-- create use => grant
create user '[user]'@'localhost' identified by '[
 password]';
grant all on *.* to '[user]'@'localhost' with grant option;
flush privileges;
-- ####################
-- 権限付与
grant all on [dbName].* to [user]@localhost;
grant all on *.* to '[user]'@'localhost' IDENTIFIED BY '[password: auth_string]';
-- ####################
-- # グローバルレベル
GRANT ALL ON *.* TO user;
GRANT SELECT, INSERT ON *.* TO user;

-- # データベースレベル
GRANT ALL ON db_name.* TO user;
GRANT SELECT, INSERT ON mydb.* TO user;

-- # テーブルレベル
GRANT ALL ON db_name.table_name TO user;
GRANT SELECT, INSERT ON db_name.mytbl TO user;

-- # カラムレベル
GRANT SELECT (col1), INSERT (col1, col2) ON db_name.table_name TO user;
-- ####################
-- 権限剥奪
revoke all on *.* from '[user]'@'localhost';

-- ユーザ削除
-- GRANT、REVOKE、SET PASSWORD、RENAME USER で操作を行った場合は特に FLUSH PRIVILEGESは不要。
-- ユーザ削除１（flush privileges不要）
DROP USER [user]@'localhost';

-- ユーザ削除２（flush privileges必要）
delete from mysql.user where user like '[user]' and host like 'localhost';
-- ユーザがメモリに残っていることを確認。
show grants for [user]@localhost; 
flush privileges;
```

##### collation
```bash

◎utf8mb4 のデフォルトはutf8mb4_0900_ai_ci
・ai: アクセントの違いを無視 (Accent Insensitive)
・ci: 大文字小文字の違いを無視

◎utf8mb4_ja_0900_as_cs
・ひらがな・カタカナ、半角全角を区別する。
・アルファベットの大文字小文字を区別する。
・拗音、濁点と半濁点はマッチしない。「びょういん」と「びよういん」、「ハハ」と「パパ」は区別される。
・絵文字は区別できる。寿司とビールはマッチしない。

◎utf8_unicode_ci
・大文字小文字、全角半角を区別しない。「パパ」を検索すると「ハハ」がヒットする。
・ただし検索結果が増えるよりも検索結果が漏れることのほうが厄介。

◎utf8mb4_bin
・UnicodeのCollationを無視。
・すべて異なる文字。

```

##### A5:SQL Mk2

```bash
ホスト名は「127.0.0.1」ではありません。
WSL2のUbuntuと接続できるIPアドレスの調べる。

> ifconfig
eth0: inet 172.xx.xxx.xxx

> ping

```

