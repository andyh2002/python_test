# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:21:50 2022

@author: xrobi
"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == "":
        break
#    catNames = catNames + [name] # 列表连接
    catNames.append(name)  # 列表增加一个元素
print('The cat names are:')
for name in catNames:
    print(" " + name)
