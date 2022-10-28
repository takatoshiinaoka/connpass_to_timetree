# connpass_to_timetree
connpassのイベントをtimetreeのカレンダーに登録するシステム

## 使い方(Github Actions)
- このリポジトリをフォークします。
- Github Actionsの環境変数を設定します。

## 使い方(ローカル)
pipenvがない場合はインストールします。
```
pipenv --version
pip install pipenv
```
ライブラリをインストールします。
```
pip install -r requirements.txt
```
仮想環境に入ります
```
pipenv shell
```
.envファイルを作成し、環境変数を設定します。
```
cp .env.example .env
```
実行します。
```
sh main.sh
```


# 参考サイト
- [【図解】作業が倍速！pipenvの使い方【Python】](https://zenn.dev/nekoallergy/articles/py-env-pipenv01)
- [TimeTree API Document](https://developers.timetreeapp.com/ja/docs/api/calendar-app)
- [connpass API リファレンス](https://connpass.com/about/api/)