#!/usr/bin/python
# coding=utf-8

#查看较大文件

import os
import sys
searchPath = '/Users/chengyi/Documents/git/kamihime/kamihime-native-app/src'
count = 0

def check_files(path, count):
    for root , dirs, files in os.walk(path):
        for name in files:
            sizeKB = os.path.getsize(os.path.join(root, name))/1024
            if sizeKB >= 0 : #and (name.endswith(".png") or name.endswith(".jpg")) 
                print ("Big File: " + os.path.join(root, name) + "    size = %d KB" %(sizeKB))
                count = count + 1
    print("count =  %d" % count)

if __name__ == "__main__":
	# searchPath = sys.argv[1]
	# print "search path: ", searchPath
	# if searchPath == "":
	# 	print "search path error"
	# 	sys.exit()
    check_files(searchPath, count)
