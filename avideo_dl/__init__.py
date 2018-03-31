import os
import argparse
from .aa import ascii_moji
from .AVideoDownloader import AVideoDownloader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URLの指定')
    parser.add_argument('-t', '--thread', help='スレッド数を指定',
                        type=int, default=10,
                        choices=[1, 10, 30, 50, 80, 100])
    args = parser.parse_args()
    print(ascii_moji['start'] + '\r')
    av = AVideoDownloader(args.url, args.thread)
    try:
        av.download()
    except KeyboardInterrupt:
        os.system('rm *.toyota')
    print('\n\n{}\n\n'.format(ascii_moji['finish']))


if __name__ == '__main__':
    main()