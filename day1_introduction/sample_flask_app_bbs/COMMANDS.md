
```bash
# Dockerイメージ作成
docker build --no-cache -t sample-flask-app-bbs:0.1 .
```


```bash
# Dockerコンテナ起動
# {path_to_your_local_dir}は適宜自分のローカルのディレクトリに読み替え
docker run --rm -v {path_to_your_local_dir}:/app -p 5000:5000 --entrypoint=/bin/bash -it  sample-flask-app-bbs:0.1
```

```bash
# 環境変数設定
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
# 今回の例ではSOME_DATABASE_URLをElephantSQLのDBのURLに読み替える
export DATABASE_URL=SOME_DATABASE_URL
```


```bash
# 起動コマンド
FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 5000 --host=0.0.0.0
```


```bash
# DB初期化
FLASK_APP=run.py flask db init
```

```bash
# DBマイグレーションファイルの作成
FLASK_APP=run.py flask db migrate
```

```bash
# DBマイグレーションの実行
FLASK_APP=run.py flask db upgrade
```

```bash
# DBマイグレーション実行前の状態に戻す
FLASK_APP=run.py flask db downgrade
```

