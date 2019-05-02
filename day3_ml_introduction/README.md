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

### 2. 動作確認
以下コマンドにより起動し、動作確認
```bash
# 起動コマンド
FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 5000 --host=0.0.0.0
```


## フロントエンドの環境構築
```sample_app_bbs\client```ディレクトリへ移動し、以下のコマンドを実行
```bash
# yarnが入ってなければ公式サイトからインストールすること
yarn install
```

以下コマンドにより、フロントエンドのアプリが起動し、ブラウザに表示される
```bash
quasar dev
```
