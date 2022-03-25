# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:50:57 2022

@author: xrobi
"""

# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')  # ask for their name
myName = input()
print("It is good to meet you," + myName)
print("The length of your name is:")
print(len(myName))
print("What is your __age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + ' in a year.')
