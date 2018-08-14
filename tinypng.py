#!/usr/bin/python
# coding=utf-8

#使用tiny png压缩图片资源

import tinify

import os
import sys
from optparse import OptionParser

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

fromPath = ''

#此key需要在官网通过邮箱申请
tinify.key = "NXg6bn8_PLP3SiZ-5my8CUjIDIBc_dgR"
# tinify.key = "9fRjqbi7XZJuEjJOK3uz__wQALb8wHXf" # cylemon2@163.com

def compress(path):
    count = 0
    for root , dirs, files in os.walk(path):
        for name in files:
            sizeKB = os.path.getsize(os.path.join(root, name))/1024
            if sizeKB > 0 and (name.endswith(".png") or name.endswith(".jpg")) :
                pngSrc = os.path.join(root, name)
                prGreen("compress++ %s" % (pngSrc))
                source = tinify.from_file(pngSrc)
                source.to_file(pngSrc)
                count = count + 1
    prLightPurple("压缩文件总数: %d" % count)

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-p", "--srcpath", dest="src_path",help='root path.')
	(opts, args) = parser.parse_args()
	fromPath = opts.src_path
	if fromPath != None:
		prLightPurple("start to compress %s " % (fromPath))
		compress(fromPath)
	else:
		prRed("Please enter the full parameters")
