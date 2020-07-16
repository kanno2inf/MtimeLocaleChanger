#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser
from datetime import datetime
from os.path import join, isfile, isdir

import pytz
from tzlocal import get_localzone


def main(argv):
    parser = ArgumentParser()
    parser.add_argument('-f', '--from', dest='from_', default='UTC')
    parser.add_argument('-t', '--to', required=False)
    parser.add_argument('paths', metavar='PATH', nargs='+', help="image file path list")
    opt = parser.parse_args(argv)

    from_ = opt.from_
    to = opt.to

    from_tz = pytz.timezone(from_)
    to_tz = pytz.timezone(to) if to else get_localzone()  # 指定されなければ現在の環境のタイムゾーン
    print(f'{from_tz} => {to_tz}')

    utc_tz = pytz.timezone('UTC')

    for dir_path in opt.paths:
        if not isdir(dir_path):
            continue
        print(dir_path)
        for filename in os.listdir(dir_path):
            # ディレクトリ内のファイルを順に変換
            img_path = join(dir_path, filename)
            if not isfile(img_path):
                continue
            # mtime取得
            stat = os.stat(img_path)
            mtime = stat.st_mtime
            # タイムゾーンを変換
            from_dt = datetime.fromtimestamp(mtime, tz=from_tz)
            to_dt = from_dt.astimezone(to_tz)
            new_mtime = to_dt.replace(tzinfo=utc_tz).timestamp()
            # ファイルのmtimeを更新
            os.utime(img_path, (stat.st_atime, new_mtime))


if __name__ == '__main__':
    main(sys.argv[1:])
