import argparse
import errno
import sys
import os
import subprocess

def makeDir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def readFile(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            text = line.split() 
            print(text) 
            subprocess.call(['ffmpeg','-y', '-i', 'featherTree5Sec.mp4', '-vf',
                             'scale=' + text[0] + ':' + text[2] + ',setsar=1:1',
                             args.dest + '/' + text[0]+text[1]+text[2] + '.' + text[4] ])

def main():
    makeDir(args.dest)
    readFile(args.input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resizes Videos")
    parser.add_argument('-d','--dest', help='output folder name')
    parser.add_argument('-i','--input', help='input file name')
    args = parser.parse_args()


    main()
