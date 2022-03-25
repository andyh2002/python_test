#! /usr/bin/env python

from math import sqrt

x = 1
while True:
    if sqrt(x+150) == int(sqrt(x+150)) and sqrt(x+150+136) == int(sqrt(x+150+136)):
        print(x)
        break
    else:
        x += 1
