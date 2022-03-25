# ！/usr/bin/env python
# _*_ coding: utf-8 _*_
import glob
import logging
import os
import pprint
import re
import time

# 指定文件目录列表
file_dir = [r'E:/test/Python_test/py_test/']
log_name = time.strftime('%Y%m%d%H%M%S') + '-' + str(os.getpid()) + '.log'
# 日志格式
logging.basicConfig(filename=log_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # 日志开关

a = set()  # 创建一个集合保存号码

for directory in file_dir:
    print('directory:', directory)
    file_list = glob.glob(directory + "*.err")

    for file_name in file_list:
        logging.debug(f'当前处理的文件为：{file_name}')
        with open(file_name, 'r', encoding='utf-8') as f:  # 指定文件编码
            # with open(r'./' + file_name, 'rb') as f:  # 或者使用rb读取二进制方式
            line_number = 0  # 记录行数
            urgent_nbr = ['10001', '10000', '10659401']  # 免费号码
            while True:  # 循环逐行处理
                line = f.readline()
                line_number += 1
                if not line:  # 记录处理完跳出循环
                    break
                logging.debug('第{%s}行: ' % line_number + line[:-1])  # 日志记录获取到的文件每行内容,去掉后面的换行符\n
                if not (file_name.find('tdl') > 0 or file_name.find('sql') > 0):  # 短信话单文件
                    sms_list = re.split(r"[ ]+", line.split('|')[1])  # 短信话单匹配多个空格进行拆分
                    logging.debug(f'第{line_number}行拆分后话单是：{sms_list}')
                    calling_nbr = sms_list[0][19:30]
                    called_nbr = sms_list[1]
                    if called_nbr in urgent_nbr:  # 短信被叫号码判断，剔除免费号码
                        logging.debug(f'主叫号码{calling_nbr}，被叫号码{called_nbr}，无需处理！')
                        continue
                    else:  # 被叫非免费号码，主叫号码加入结果结合中
                        logging.debug(f'主叫号码{calling_nbr}，被叫号码{called_nbr}')
                        a.add(calling_nbr)
                else:  # 语音话单文件
                    cdr_list = line.split('|')
                    logging.debug(f'第{line_number}行拆分后话单是：{cdr_list}')
                    billing_nbr = cdr_list[2]
                    calling_nbr = cdr_list[4]
                    called_nbr = cdr_list[5]
                    logging.debug(f'第{line_number}行拆分后话单中：计费号码{billing_nbr}，主叫号码{calling_nbr}，被叫号码{called_nbr}')
                    if (billing_nbr == calling_nbr and called_nbr in urgent_nbr) or \
                            (billing_nbr == called_nbr and calling_nbr in urgent_nbr):
                        logging.debug(f'主叫号码{calling_nbr}，被叫号码{called_nbr}，无需处理！')
                        continue
                    else:
                        a.add(billing_nbr)
                        logging.debug(f'add number {billing_nbr}')
        f.close()
# print(a)
pprint.pprint(a)
