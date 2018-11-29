# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:52:18 2018

@author: Administrator
"""

#第16章  文件的处理
import csv
#尝试文件读取
filename = 'wechat_friends.csv'
with open(filename, encoding='UTF-8') as f_obj:
    reader = csv.reader(f_obj)
    #header = next(reader)
    citys = []
    for row in reader:
        citys.append(row[2])
    print(citys)
    
#使用datetime类
from datetime import datetime
firstdate = datetime.strptime('2018-11-2', '%Y-%m-%d')
print (firstdate)

#图表＋csv文件操作练习
from matplotlib import pyplot as plt
with open(filename, encoding='UTF-8') as f_obj:
    reader = csv.reader(f_obj)
    header = next(reader)
    cities = []
    for row in reader:
        cities.append(row[2])
city_names = list(set(cities))
counts = []
for cityname in city_names:
    counts.append(cities.count(cityname))
plt.figure(1,figsize=(10,10))
#width = 1.0
#city_names = [x * width for x , _ in enumerate(city_names)]
plt.bar(range(len(city_names)), counts, tick_label=city_names)









