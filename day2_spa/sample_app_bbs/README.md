# Day2: 掲示板サンプル SPA版

## 概要
day1にて作成した掲示板アプリを、SPA(Single Page Application)にする
フロントエンド側はVue.jsにて実装し、APIサーバー側はFlask、DBは引き続きPostgreSQLとする
フロントエンド実装は簡素化のため、Quasar(https://quasar-framework.org/)を使用

## 前提条件
* day1_introductionの内容が完了できていること
* ElephantSQL (https://www.elephantsql.com/) のアカウントを持っていること(フリープランでOK)
* Node.jsがインストール済みであること


## サーバー側の環境構築
### 起動のための環境変数設定
```bash
# 環境変数設定
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
# 今回の例ではSOME_DATABASE_URLをElephantSQLのDBのURLに読み替える
export DATABASE_URL=SOME_DATABASE_URL
```

### 1. DBの初期設定
以下コマンドによりDB初期化(migrationsフォルダ作成)
```bash
FLASK_APP=migrate.py flask db init
```

以下コマンドによりmodelに定義された内容をDBに反映させるためのファイルを生成
```bash
FLASK_APP=migrate.py flask db migrate
```

以下コマンドにより、上記で生成したmigration用のファイルの内容をDBに反映
```bash
FLASK_APP=migrate.py flask db upgrade
```

以下コマンドにより起動し、動作確認
```bash
# 起動コマンド
FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 5000 --host=0.0.0.0
```


## XX. フロントエンドの環境構築
XXXXXXXXXX



## 練習1. このアプリをローカルで実行する
今回のサンプルでは、DBにPostgreSQLを使用することを想定。
COMMANDS.mdにセットアップコマンドおよび起動コマンドを記載


## 練習2. このアプリをHerokuにデプロイする
以下の様なコマンドにより、Heroku上での環境変数を設定。
DB接続情報や、ローカルで設定した環境変数は、Heroku上でも設定する必要がある。
```bash
# https://devcenter.heroku.com/articles/config-vars に記載の例
heroku config:set GITHUB_USERNAME=joesmith
```

## 練習3. アプリに機能を追加する
現在は、
* テキストを投稿する機能
* 投稿されたテキストを一覧表示する機能

のみが実装されている。

例えば、以下のような機能を追加してみる
* 投稿を削除する機能
* 名前欄に「fusianasan」と入力された投稿はIPアドレスを表示する機能
* デザインを変える (なお、今回のサンプルはBootstrapのテンプレート (https://startbootstrap.com/themes/clean-blog/) をほぼそのまま流用)


