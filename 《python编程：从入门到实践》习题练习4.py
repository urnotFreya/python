# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:31:14 2018

@author: Administrator
"""
#1.简单的文件读取操作
'''
with open('thehouseprice.txt') as file_object:
    #price = file_object.read()
    #print(price)
    lines = file_object.readlines()
pi = ''
for line in lines:
    pi += line.strip()
print(pi)
print(len(pi))
'''
#2.在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的 Python 知识，其中每一
#行都以 “In Python you can” 打头。将这个文件命名为learning_python.txt ，并将其存
#储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，并将你所
#写的内容打印三次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时
#将各行存储在一个列表中，再在 with 代码块外打印它们。
'''
filename = 'fileTest.txt'
pi = []
with open(filename) as file_object:
    #content = file_object.read()
    #print(file_object)
    #for line in file_object:
     #   print(line)
    lines = file_object.readlines()
print(lines)
'''
#3.文件写入练习
'''
with open('thehouseprice.txt','r+') as file_object:
    file_object.write("我做个测试啦，看看先前的文件还在不在咯")
    file_object.seek(0)
    content = file_object.read()
    print(content)
'''
#4.编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语
#并将一条访问记录添加到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一行。
'''
while True:
    guest_name = input('请输入名字：')
    if(guest_name == 'q'):
        break
    print (guest_name + " Welcome to my programming game!")
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(guest_name + '访问该文件！\n')
with open ('guest_book.txt') as fo:
    content = fo.read()
    print(content)
'''
'''
string = "hello   world!"
l = string.split()
print (len(l))    
'''


#5.访问项目 Gutenberg （ http://gutenberg.org/），并找一些你想分析的图书。下载这
#些作品的文本文件或将浏览器中的原始文本复制到文本文件中。你可以使用方法 count() 
#来确定特定的单词或短语在字符串中出现了多少次。
'''
count_words.py
count = 0
def conut_words(filename):
    try :
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print ("Sorry,the " + filename +"not found!")
    else:
        file_list = content.split()
        count = len(file_list)
    return count
'''
'''
from count_words import conut_words as  count_words
words1 = count_words('Alice.txt')
words2 = count_words('Knight.txt')
words3 = count_words('freya.txt')
print (words1)
'''

#6.编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump() 将这个数字存储到文件
#中。再编写一个程序，从文件中读取这个值，并打印消息 “I know your favorite number!
# It's _____.” 。
#7.记住喜欢的数字 ：将练习 6 中的两个程序合而为一。如果存储了用户喜欢的数字，
#就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，
#看看它是否像预期的那样工作。
import json
temp = input("请输入你喜欢的数字：")
number = int(temp)
with open('favorite_number.json','w') as f_obj:
    #f_obj.write(temp)
    json.dump(number, f_obj)
try:
    with open('favorite_number.json') as f_obj:
        #content = f_obj.read()
        content = json.load(f_obj)
        print ("Your fa number is "+ str(content))
except FileNotFoundError:
    print("没有存储过任何数据")
























