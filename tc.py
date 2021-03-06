#!/usr/bin/env python3
from decompressor import TextDecompressor
from compressor import TextCompressor
import argparse

parser = argparse.ArgumentParser(description='Compresses or decompresses text files.')
parser.add_argument('file_name', nargs=1, metavar='file name', help='The name of the file to be processed.')
parser.add_argument('-d', help='Decompress the file (defaults to compressing).', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':
    if args.d:
        print('decompressing', args.file_name[0])
        decompressor = TextDecompressor(args.file_name[0])
        decompressor.decompress()
    else:
        print('compressing', args.file_name[0])
        compressor = TextCompressor(args.file_name[0])
        compressor.compress()
