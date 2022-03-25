#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import time

# 程序入口
if __name__ == '__main__':
    staffCounts = input("请输入员工总人数 : ")
    print("请输入员工姓名，职级，工作年限，工资信息，空格隔开：")
    dicStaff = {}
    lstStaff = []
    for n in range(0, int(staffCounts)):
        print("第%03d位员工: " % (n + 1), end="")
        infoStaff = input()
        lstValue = infoStaff.split(" ")
        while len(lstValue) != 4:
            print("输入格式有误，请重新输入：", end="")
            infoStaff = input()
            lstValue = infoStaff.split(" ")
        if dicStaff.get(infoStaff) is None:
            dicStaff[infoStaff] = lstValue
        else:
            print("输入重复：%s" % infoStaff)
            continue
        lstStaff.append(lstValue)
    # lstStaff.append(["张三", 3, 3, 3000])
    # lstStaff.append(["李四", 3, 4, 3000])
    # lstStaff.append(["王五", 3, 3, 3000])
    # lstStaff.append(["赵六", 4, 3, 3000])
    # lstStaff.append(["陆奇", 4, 4, 4000])
    # lstStaff.append(["炎八", 4, 4, 3980.99])
    tupleStaff = tuple(lstStaff)
    # tupleStaff.sort(key=lambda x: (-x[1], x[3], -x[2]))
    tupleStaffTmp = sorted(tupleStaff, key=lambda x: (-int(x[1]), float(x[3]), -int(x[2])))  # 排序关键字
    lstStaff = list(tupleStaffTmp)
    print("最终排序结果如下：")
    for lstTmp in lstStaff:
        print("%s %s %s %s" % (str(lstTmp[0]), str(lstTmp[1]), str(lstTmp[2]), str(lstTmp[3])))
