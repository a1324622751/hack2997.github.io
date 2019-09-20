#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

def mergedomain():
    #打开导output目录下的所有xt文件，然后合并output
    list=[]
    merged_url_file=open("output/merged_url_file.txt",'w')
    file=open("output/domain_from_js.txt",'r')
    file1=open("teemo/output/domain_from_teemo.txt",'r')
    list1 = os.listdir(os.getcwd())
    for txt in list1:
        if txt.endswith(".txt"):
            url=txt
    file2=open(url,'r')
    for lin in file.readlines():
        list.append(lin)
        merged_url_file.write(lin)
    for lin in file1.readlines():
        try:
            lin.index('@')
        except ValueError:
            try:
                list.index(lin)
            except ValueError:
                list.append(lin)
                merged_url_file.write(lin)
    for lin in file2.readlines():
        if(lin!="subdomain"):
            try:
                list.index(lin)
            except ValueError:
                list.append(lin)
                merged_url_file.write(lin)
    merged_url_file.close()
    file.close()
    file1.close()
    file2.close()