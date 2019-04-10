# Day1-2: 掲示板サンプル 

## 前提条件
* day1_introductionの内容が完了できていること
* ElephantSQL (https://www.elephantsql.com/) のアカウントを持っていること(フリープランでOK)


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


