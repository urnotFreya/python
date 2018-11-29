# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:31:31 2018

@author: Administrator
"""

def conut_words(filename):
    count = 0
    try :
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print ("Sorry,the " + filename +"not found!")
    else:
        file_list = content.split()
        count = len(file_list)
    return count