#!/usr/bin/python
# coding=utf-8
# 

#部署apk、ipa到Fir

import requests
from optparse import OptionParser

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

def deploy(platform, package_name, app_name, version, build_version, apk_path, icon_path, change_log):
    data = {'type': platform, 'bundle_id': package_name,
            'api_token': '1b21ba8a145d6f8de08448b6bf0e7c65'}
    req = requests.post(url='http://api.fir.im/apps', data=data)
    content = req.json()
    prGreen('上传资质：' + str(content))
    icon_dict = content['cert']['icon']
    binary_dict  = content['cert']['binary']

    #上传apk
    try:
        prLightPurple("上传apk")
        apk_path = apk_path
        file = {'file': open(apk_path, 'rb')}
        param = {"key": binary_dict['key'],
                 "token": binary_dict['token'],
                 "x:name": app_name,
                 "x:version": version, 
                 "x:build": build_version, 
                 "x:changelog": change_log}
        req = requests.post(url = binary_dict['upload_url'], files=file, data=param, verify=False)
        prGreen('success_apk: ' + req.content)
    except Exception as e:
        prRed('error_apk: ' + e)

    #上传Logo
    try:
        prLightPurple('上传Logo')
        icon_path = icon_path
        file = {'file': open(icon_path, 'rb')}
        param = {
            "key": icon_dict['key'],
            "token": icon_dict['token']}
        req = requests.post(url=icon_dict['upload_url'], files=file, data=param, verify=False)
        prGreen('success_icon: ' + req.content)
    except Exception as e:
        prRed('error_icon: ' + e)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--platfrom", dest="platfrom",help='platfrom.')
    parser.add_option("-p", "--package", dest="package_name",help='package name.')
    parser.add_option("-v", "--version", dest="app_version",help='app version.')
    parser.add_option("-b", "--versionnum", dest="build_version",help='build version.')
    parser.add_option("-n", "--name", dest="app_name",help='app name.')
    parser.add_option("-a", "--apkpath", dest="apk_path",help='apk path.')
    parser.add_option("-i", "--iconpath", dest="icon_path",help='icon path.')
    parser.add_option("-l", "--changelog", dest="change_log",help='change log.')
    (opts, args) = parser.parse_args()

    platfrom = opts.platfrom
    apk_path = opts.apk_path
    icon_path = opts.icon_path
    app_version = opts.app_version
    build_version = opts.build_version
    app_name = opts.app_name
    change_log = opts.change_log
    package_name = opts.package_name

    prPurple("平台: " + str(platfrom))
    prPurple("包名: " + str(package_name))
    prPurple("应用名: " + str(app_name))
    prPurple("应用版本号: " + str(app_version))
    prPurple("打包版本号: " + str(build_version))
    prPurple("apk路径: " + str(apk_path))
    prPurple("icon路径: " + str(icon_path))
    prPurple("修改内容: " + str(change_log))

    if platfrom and apk_path and icon_path and app_version and build_version and app_name and change_log and package_name:
        deploy(platfrom, package_name, app_name, app_version, build_version, apk_path, icon_path, change_log)
    else:
        prRed("部分参数不存在，请修改后重试！！！")



    # 

