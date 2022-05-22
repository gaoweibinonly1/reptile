#coding=utf-8
import requests
import re
import os
import time

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

if __name__ == '__main__':
    url_base = 'https://img.f2mm.com/gallery3'
    data = 20220519
    level = 26161
    pos = 1
    path = '/root/Pictures/'

    while level > 0:
        tmp_path = path + '/' + str(level) # 组号是唯一的
        mkdir(tmp_path)
        tmp_url = url_base + '/' + str(data) + '/' + str(level)
        
        while pos > 0:
            down_url = tmp_url + '/' + str(pos) + '.jpg'
            myfile = requests.get(down_url)   
            if (myfile.status_code == 200):
                filename = tmp_path + '/' + str(pos) + '.jpg'
                open(filename, 'wb').write(myfile.content)
                pos += 1
            else:
                if (pos == 1):
                    data -= 1
                else :
                    level -= 1
                    pos = 1;
                break
        print("data is %s, level is %d", (level, data))
