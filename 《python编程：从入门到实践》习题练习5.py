# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:14:42 2018

@author: Administrator
"""
'''
nametest.py
def get_formatted_name(firstname, lastname):
    full_name = firstname + " " + lastname
    return full_name.title()
'''


#基本测试函数练习
'''
import unittest
from nametest import get_formatted_name
class NameTestCase(unittest.TestCase):
    def test_nameformat(self):
        formatted_name = get_formatted_name('freya', 'Liu')
        self.assertEqual(formatted_name, 'Freya Liu')
unittest.main()
'''        
#1.城市和国家 ：编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个
#格式为 City, Country 的字符串，如 Santiago, Chile 。将这个函数存储在一个名为 
#city_functions.py 的模块中。创建一个名为 test_cities.py 的程序，对刚编写的函数进
#行测试（别忘了，你需要导入模块 unittest 以及要测试的函数）。编写一个名为 
#test_city_country() 的方法，核实使用类似于 'santiago' 和 'chile' 这样的值来调用
#前述函数时，得到的字符串是正确的。运行 test_cities.py ，确认测试
# test_city_country() 通过了。
#2.人口数量 ：修改前面的函数，使其包含第三个必不可少的形参 population ，并返回一个
#格式为 City, Country - population xxx 的字符串，
#如 Santiago, Chile - population 5000000 。
#运行 test_cities.py ，确认测试 test_city_country() 未通过。
#修改上述函数，将形参 population 设置为可选的。再次运行 test_cities.py ，
#确认测试 test_city_country() 又通过了。再编写一个名为 
#test_city_country_population() 的测试，核实可以使用类似于 'santiago' 、 'chile'
#和 'population=5000000' 这样的值来调用这个函数。再次运行 test_cities.py ，
#确认测试 test_city_country_population() 通过了。
'''
city_function.py
def city_format(city_name, country_name, population):
    formatted_name = city_name.title() + "," + country_name.title() + " - population" + population  

    return formatted_name
'''
'''
import unittest
from city_function import city_format
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_format('shanghai', 'china')
        self.assertEqual(formatted_name, 'Shanghai,China')
    def test_city_country_population(self):
        formatted_name = city_format('shanghai', 'china', '9000')
        self.assertEqual(formatted_name, 'Shanghai,China - population9000')
unittest.main()
'''
'''
编写一个名为 Employee 的类，其方法 __init__() 接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法： test_give_default_raise() 和 test_give_custom_raise() 。使用方法 setUp() ，以免在
每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
'''
import unittest
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self,add=5000):
        self.salary += add

        
class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('freya', 8000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 13000)
    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.salary, 16000)
unittest.main()
        
    





















