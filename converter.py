import sys
import codecs
import argparse
from phoneme_util import PhonemeUtil
from mora_util import MoraUtil

def main():
    parser = argparse.ArgumentParser()
    parser = argparse.add_argument('--code', type=str, default='char', help='[char|mora|phone]')
    args = parser.parse_args()

    for line in sys.stdin.buffer:
        line = line.decode("utf-8").strip()
        if args.code == 'char':
            tokens = line.split(//)
        elif args.code == 'mora':
            tokens = MoraUtil.kana2mora(line)
        elif args.code == 'phone':
            tokens = PhonemeUtil.kana2phone(line)
        else:
            raise ValueError("invalid code %s" % args.code)

if __name__ == '__main__':
  main()
