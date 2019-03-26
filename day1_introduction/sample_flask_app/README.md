# Day1: ローカルでDockerコンテナ作成→Herokuデプロイするサンプル

## 前提条件
* Dockerのセットアップが完了していること
* Herokuのアカウントを持っていること(フリープランでOK)


## 1. Dockerfileからイメージを作成
以下のコマンドを実行。flask-sampleの部分は作成するイメージの名称。適宜書き換えてOK
```bash
docker build -t flask-sample:0.1 .
```

## 2. イメージからコンテナを起動&ローカルのフォルダと同期
 (これがないと、ファイルの編集にIDE等が使えない)
 
 下記の場合、アプリを起動すればlocalhost:5000で動作確認可能
```bash
# {path_to_your_local_dir}は適宜自分のローカルのディレクトリに読み替え
docker run --rm -v {path_to_your_local_dir}:/app -p 5000:5000 --entrypoint=/bin/bash -it flask-sample:0.1 
```

## 3. コンテナ上で動作確認
```bash
python app.py

# 以下のようなメッセージが出れば成功
#  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
#  * Restarting with stat
#  * Debugger is active!
```
以下にアクセスするとページが表示される

http://localhost:5000/

## 4. Herokuへデプロイ
まずはherokuにログイン
```bash
heroku login
```

以下のようなメッセージが出るので、任意のキーを押す
```bash
# heroku: Press any key to open up the browser to login or q to exit:
```
以下のようにURLが出てくるので、これをブラウザにコピペしてアクセス
```bash
# Opening browser to https://cli-auth.heroku.com/auth/browser/xxxxxxxxxxx
#  ›   Warning: Cannot open browser.
# heroku: Waiting for login... ⢿
``` 
以下のコマンドによりローカルブランチへ差分をコミットしておく
```bash
git init
git status
git add .
git commit -m "initial commit"
```

以下コマンドにより、heroku上にアプリを作成&Gitの紐づけ
```bash
heroku apps:create some_app_name
heroku git:remote -a some_app_name
```

以下コマンドによりHerokuにデプロイ
```bash
git push heroku master
```
