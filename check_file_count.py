#!/usr/bin/python
# coding=utf-8
#tes
#查看文件夹内包含文件的数量

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

tinify.key = "uxge7YFOZ8i-XCJgj2qCCKNMM3oxrVU8"

def check(path, filetype):
	count = 0
   	for root , dirs, files in os.walk(path):
		for name in files:
			sizeKB = os.path.getsize(os.path.join(root, name))/1024
			if sizeKB > 0 and filetype and (name.endswith("."+filetype)):
				count = count + 1
			elif filetype == None :
				count = count + 1
   	return count

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-p", "--srcpath", dest="src_path",help='root path.')
	parser.add_option("-t", "--filetype", dest="file_type",help='file type.')
	(opts, args) = parser.parse_args()
	opts.src_path
	if opts.src_path != None :
		count = check(opts.src_path, opts.file_type)
		prLightPurple("路径：%s 文件类型: %s 总数: %d" % (opts.src_path, opts.file_type or "*", count) )
	else:
		prRed("Please enter the full parameters use -h chekc more")
