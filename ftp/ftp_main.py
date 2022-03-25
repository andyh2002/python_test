# coding=utf-8
from ftplib import FTP
import re
# python---FTP批量下载/删除/上传


# 1、连接ftp
def ftpconnect(ftpserver, port, username, password):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
    except:
        raise IOError('FTP connect failed!')

    try:
        ftp.login(username, password)
    except:
        raise IOError('FTP login failed')
    else:
        print("**********地址：", ftpserver, "用户：", username, "连接登录成功**********")
        return ftp


# 2、FTP文件批量下载
def ftpdownload(ftp, localpath, ftppath):
   # 读取ftppath路径下的文件，选择日期并存放在一个数组中
    a = input(u"请输入下载文件的日期，如：20180612")
    # 注意两点：1、正则表达式变量要加str 2、获取的文件名列表要转换成str
    n = ftp.nlst(ftppath)  # 获取ftppath中的文件名，返回一个列表
    t1 = re.compile(r'')
    list1 = t1.findall(str(n))
    bufsize = 1024*1024

    print("**********开始下载**********")
    # socket.setfefaulttimeount(1)
    for i in list1:
        loop = 0

        while loop < 3:
            try:
                file_handle = open(localpath + i, 'wb').write
                ftp.retrbinary('RETR %s' % i, file_handle, bufsize)
                print('access', i)
                break
            except:
                loop = loop + 1
                print('error', i)
    print("**********下载完成**********")


# 3、FTP文件批量删除
# 根据日期批量删除ftp上的文件
def delftpfile(ftp, ftppath):
    a = input(u"请输入要删除文件的日期,如：20180612")
    n = ftp.nlst(ftppath)  # 获取ftppath中的文件名，返回一个列表
    t1 = re.compile(r'')
    list1 = t1.findall(str(n))
    print("**********开始删除文件**********")
    for i in list1:
        try:
            ftp.delete(i)
            print(i, "删除成功")
        except:
            print(i, "删除失败@@@@@@@@@@")
    print("**********文件删除完毕**********")


# 4、FTP文件上传
# 向ftp上指定的文件目录上传文件
def uploadfile(ftp, localpath, ftppath):
    try:
        name = '1.txt'
        path = localpath + name
        ftp.storbinary('STOR ' + name, open(path, 'rb'))
        print(name, "上传成功")
    except:
        print(name, "上传失败")


# 5、FTP关闭连接
def ftpclose(ftp):
    ftp.quit()
    print("**********ftp退出**********")


#  main函数
if __name__ == "__main__":
    ftp = ftpconnect('134.64.105.155', 21, 'ftp_ias', 'vv1#k2at')
    ftpclose(ftp)
