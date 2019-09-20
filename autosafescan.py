#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import importlib
import urllib
import MergeDomain
import get_titile
import subdomainfindclass

def main():
    print ("usage:autosafescan -u xxxxx")
if __name__=='__main__':
    main()
    url=input("target:")
    jsurlpath=""
    # /代表当前目录
    list1=os.listdir(os.getcwd())
    for txt in list1:
        if txt.endswith(".txt"):
            jsurlpath=txt
            os.remove(txt)
    subdomainfindclass.SubdomainFinder(url)
    MergeDomain.mergedomain()
    print("begin get title:")
    ip_file="output/merged_url_file.txt"
    os.system("python2 get_titile.py "+ip_file)
    print("end get title:")
    print("Congratulations! You succeeded!")
