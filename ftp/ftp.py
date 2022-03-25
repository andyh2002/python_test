# coding=utf-8
from ftplib import FTP
import os
import re

ftp = FTP("134.64.105.155")
ftp.login("ftp_ias", "vv1#k2at")
ftp.encoding = 'utf-8'
# print(ftp.getwelcome())
# ftp.retrlines('LIST')
ftp.cwd('swgj')
# ftp.retrlines('LIST')
# print(ftp.dir())

n = ftp.nlst('')  # 返回一个文件名列表
# for name in n:
#     print(name)
print(str(n))

t1 = re.compile(r'\w+20200701\w+\.dat')
list1 = t1.findall(str(n))
print('********开始删除文件********')
for i in list1:
    try:
        ftp.delete(i)
        print(i, '删除成功')
    except:
        print(i, '删除失败！')
print('********文件删除完毕!********')
