# MtimeZoneChanger

ファイル更新日時のタイムゾーンを一括変換するスクリプト

## 動作環境
python3.6.x

## 使い方

必要モジュールインストール
```bash
$ pip install -r requirements
```

ファイルを含むディレクトリパスを指定して実行。(複数指定可能)
```bash
$ python3 changer.py "DIRECTORY_PATH"
```


```bash
usage: changer.py [-h] [-f FROM_] [-t TO] PATH [PATH ...]

positional arguments:
  PATH                  image file path list

optional arguments:
  -h, --help            show this help message and exit
  -f FROM_, --from FROM_ 現在の更新時刻のタイムゾーン
  -t TO, --to TO        書き換え後の更新時刻のタイムゾーン
```

`-f`はデフォルトでUTC、`-t`はデフォルトでシステムのタイムゾーンが指定されています。

複数回同じファイルに適用するとタイムゾーンがずれていくので注意。