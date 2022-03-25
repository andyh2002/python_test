# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:19:01 2022

@author: xrobi
"""

import sys

while True:
    print("Type exit to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
