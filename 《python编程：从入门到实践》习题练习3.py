# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:23:13 2018

@author: Administrator
"""

#<<python编程：从入门到实践>>第九章
#1.建一个名为 User 的类，其中包含属性 first_name 和 last_name ，还有用户简介通常会
#存储的其他几个属性。在类 User 中定义一个名为 describe_user() 的方法，它打印用户信息
#摘要；再定义一个名为 greet_user() 的方法，它向用户发出个性化的问候。创建多个表示不同
#用户的实例，并对每个实例都调用上述两个方法。
'''
class User():
    def __init__(self,first_name,last_name,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user( *info ):
        print('用户信息：')
        print(info)
    def greet_user(self):
        print("hello,"+self.first_name+"!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
'''    
'''
user1 = User('freya','Liu');
user1.describe_user("laugh","up")
user1.greet_user();

user2 = User('Chris', 'Lee')
user2.describe_user("singer");
'''
#2.尝试登录次数 ：在为完成练习 9-3 而编写的 User 类中，添加一个名为 login_attempts
# 的属性。编写一个名为 increment_login_attempts() 的方法，它将属性 login_attempts
#的值加 1 。再编写一个名为 reset_login_attempts() 的方法，它将属性 login_attempts
#的值重置为 0 。根据 User 类创建一个实例，再调用方法 increment_login_attempts() 
#多次。打印属性 login_attempts 的值，确认它被正确地递增；然后，调用方法 
#reset_login_attempts() ，并再次打印属性 login_attempts 的值，确认它被重置为 0 
'''
user1 = User('freya','Liu',1)
for i in range(5):
    user1.increment_login_attempts();
user1.increment_login_attempts();
print(user1.login_attempts)
user1.reset_login_attempts();
print(user1.login_attempts)
'''
#3.冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承Restaurant
#类。这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 
#的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。
#创建一个 IceCreamStand 实例，并调用这个方法。
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("餐馆信息："+self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        print("餐馆正在营业！")
'''
'''
r = Restaurant("freya", "川菜")
r.describe_restaurant()
r.open_restaurant()
'''
'''
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    def set_iceType(self, *infos):
        self.flavours = [];
        for info in infos:
            self.flavours.append(info)
    def describe_ice(self):
        for flavour in self.flavours:
            print ("冰淇淋的口味：" )
            print (flavour)
ii=IceCreamStand("freya","Ice")
ii.set_iceType('haha','hehe')
ii.describe_ice()
'''

#4.管理员是一种特殊的用户。编写一个名为 Admin 的类，添加一个名为 privileges 的属性，
#用于存储一个由字符串（如 "can add post" 、 "can delete post" 、 "can ban user" 
#等）组成的列表。编写一个名为 show_privileges() 的方法，它显示管理员的权限。创建
#一个 Admin 实例，并调用这个方法。


#5.编写一个名为 Privileges 的类，它只有一个属性 —— privileges ，其中存储了上述习题 
#所说的字符串列表。将方法 show_privileges() 移到这个类中。在 Admin 类中，将一个 
#Privileges 实例用作其属性。创建一个 Admin 实例，
#并使用方法 show_privileges() 来显示其权限。
'''
class Admin(User):
    def __init__(self,first_name,last_name,login_attempts=0):
        super().__init__(first_name,last_name,login_attempts=0)
        self.privileges = Privileges(
                                     ["can add post",
                                      "can delete post",
                                      "can bam user"]
                                      )
        #self.privileges=[]
        #for privilege in privileges:
         #   self.privileges.append(privilege)
    #def show_privileges(self):
     #   print(self.privileges)


    
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)
admin = Admin("freya","Liu",0)
admin.privileges.show_privileges()
'''
#6.将 User 、 Privileges 和 Admin 类存储在一个
#模块中，再创建一个文件，在其中创建一个 Admin 实例并对其调用方法 show_privileges() 
#以确认一切都能正确地运行。
'''
from user import Admin
admin = Admin("freya", "Liu")
admin.privileges.show_privileges()
'''
#7.使用有序字典
from collections import OrderedDict 
temp = OrderedDict()
temp['firstName'] = "freya"
temp['lastName'] = 'Liu'
for firstName,lastName in temp.items():
    print("firstName:" + firstName)
    print('lastName:' + lastName)





