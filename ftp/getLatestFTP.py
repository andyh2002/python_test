#! /usr/bin/env python

import ftplib
import os
import socket

HOST = '134.64.105.155'
DIRN = 'swgj'
FILE = 'sql.txt'


def main():
    try:
        f = ftplib.FTP(host=HOST, user='ftp_ias', passwd='vv1#k2at')
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach %s' % HOST)
        return
    print("*** Connected to host %s" % HOST)

    # 匿名账户登录
    # try:
    #     f.login()
    # except ftplib.error_perm:
    #     print('ERROR: Cannot login anonymously')
    #     return
    # print("*** Logged in as 'anonymous'")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("ERROR: cannot CD to %s" % DIRN)
        f.quit()
        return
    print("*** Changed to %s folder" % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)  # 传递了一个回调函数保存接收到的文件
    except ftplib.error_perm:
        print("ERROR: cannot read file %s" % FILE)
        os.unlink(FILE)
    else:
        print("*** Downloaded %s to CWD" % FILE)


main()
# if __name__ == "__main__":
#     main()
