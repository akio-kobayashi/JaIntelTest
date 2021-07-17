import sys
import codecs
import argparse
from phoneme_util import PhonemeUtil
from mora_util import MoraUtil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True, help='input file')
    parser.add_argument('--code', type=str, default='char', help='[char|mora|phone]')
    args = parser.parse_args()

    if args.code == 'mora':
        ut=MoraUtil()
    elif args.code == 'phone':
        ut=PhonemeUtil()

    with open(args.file, 'r') as f:
        lines = f.readlines()

    num=1
    for line in lines:
        line = line.strip()
        if args.code == 'char':
            tokens = list(line)
        elif args.code == 'mora':
            tokens = ut.kana2mora(line)
        elif args.code == 'phone':
            tokens = ut.kana2phone(line)
        else:
            raise ValueError("invalid code %s" % args.code)
        line = ' '.join(tokens)
        print(line + ' (' + str(num).zfill(3) +')')
        num+=1
        
if __name__ == '__main__':
  main()
