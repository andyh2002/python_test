# coding=utf-8
from ftplib import FTP
import os
import re
import sys
import getopt

ftp = FTP("134.64.105.155")
ftp.login("ftp_ias", "vv1#k2at")
ftp.encoding = 'utf-8'
ftp.cwd('swgj')
n = ftp.nlst('')  # 列出文件
# print(str(n))
t1 = re.compile(r'\w+20200701\w+\.dat')  # 正则表达式匹配
list1 = t1.findall(str(n))
print('--------开始删除文件--------')
for i in list1:
    try:
        ftp.delete(i)
        print(i, '删除成功')
    except:
        print(i, '删除失败！')
print('--------文件删除完毕--------')

