# Day3: 機械学習環境構築

## 概要
機械学習用の環境を構築します。
Kaggleの公式のDockerイメージをpullします。


## 前提条件
* day2_spaまでの内容が完了できていること


### Dockerイメージの作成
以下コマンドによりイメージ作成
```bash
docker build -t kaggle-sandbox:0.1 .
```

### Jupyter Notebookの動作確認
以下コマンドによりコンテナ起動&Jupyter Notebookを起動
```bash
# {path_to_your_local_dir}は適宜自分のローカルのディレクトリに読み替え
docker run -v {path_to_your_local_dir}:/tmp/working -w=/tmp/working -p 8888:8888 --rm -it kaggle-sandbox:0.1 jupyter notebook --no-browser --ip="0.0.0.0" --notebook-dir=/tmp/working --allow-root
```

上記が成功すると、tokenが表示されるはず。
```localhost:8888```にアクセスし、上記で出力されたtokenを入力することでNotebookの利用が可能になる

以降、```titanic_sample\notebooks\Titanic Sample Notebook.ipynb```に沿って実行
