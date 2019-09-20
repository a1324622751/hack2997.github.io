#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import sys
import os
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def get_title(req):
    title_web = re.findall('<TITLE>(.*?)</TITLE>', req.text, re.I)
    t_web = ''.join(title_web)
    # title_mgr = re.findall('<TITLE>(.*?)</TITLE>', req.text, re.I)
    # t_mgr = ''.join(title_mgr).encode('utf-8')
    if t_web == '':
        return 'N/A'
    else:
        return t_web

def get_banner(req):
    if 'Server' in req.headers:
        return req.headers['Server']
    else:
        return "N/A"

def server_conn(url):
    try:
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url, timeout=10, verify=False)
        return req
    except Exception as err:
        pass

def get_webinfo(req, url):
    try:
        title = get_title(req).encode('UTF-8')
        banner = get_banner(req).encode('UTF-8')
        #print (url + " | " + title + " | " + banner)
        Accessable_file.write(url + " | " + title + " | " + banner+"\n")
        #comand = "python dirsearch//dirsearch.py -u " + url + " -e jsp"
        #print(comand)
        #os.system(comand)
    except Exception as err:
        pass

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ip_file = sys.argv[1]
    Accessable_file=open("output/Accessable_url_file.txt",'w+')
    # ip_file = sys.argv[1] # python get_title.py file.name
    for line in open(ip_file, 'a+'):
        url = 'http://' + line.strip()
        url_ssl = 'https://' + line.strip()
        req = server_conn(url)
        if req is not None:
            if req.status_code == 400:
                get_webinfo(server_conn(url_ssl), url_ssl)
            else:
                get_webinfo(req, url)
    Accessable_file.close()