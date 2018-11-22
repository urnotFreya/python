# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:49:28 2018

@author: Administrator
"""

#<<python编程：从入门到实践>>第八章部分习题
#1.编写一个名为 describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
#这个函数应打印一个简单的句子，如 Reykjavik is in Iceland 。
#给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''
def describe_city(city_name, country = 'Null'):
    print(city_name + " is in " + country)
describe_city('shanghai','china')
describe_city(country = 'PB' ,city_name = 'freya')
describe_city("havard")
'''
#2.编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可
#少的信息，以及两个名称 — 值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
'''
import mycar
car = mycar.mycar('subaru', 'outback', color='blue', tow_package=True)
print (car)
'''
