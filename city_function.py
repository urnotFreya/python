# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:14:02 2018

@author: Administrator
"""
'''
def city_format(city_name, country_name):
    formatted_name = city_name.title() + "," + country_name.title()
    return formatted_name
'''

def city_format(city_name, country_name, population='' ):
    if population:
        formatted_name = city_name.title() + "," + country_name.title() + " - population" + population
    else:
        formatted_name = city_name.title() + "," + country_name.title() 
    return formatted_name  
