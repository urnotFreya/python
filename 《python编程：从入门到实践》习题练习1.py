#<<python 编程:从入门到实践>>习题练习'第七章
#1.让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
'''
message = input ("Please input a number")
num = int (message)
if num % 10 == 0 :
    print ("Yes")
else :
    print ("NO")
''' 

#2.有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费； 3~12 岁的观众为 10 美元；
#超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
#在 while 循环中使用条件测试来结束循环。
#使用变量 active 来控制循环结束的时机。
#使用 break 语句在用户输入 'quit' 时退出循环。
'''
active = True
while active :
    message = input("The age: ")
    if message == 'quit':
        break
    age = int (message)
    if age < 3 :
        print ("Free!")
    elif age < 12 :
        print ("$10!")
    else :
        print ("$15")
'''
#3.熟食店 ：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一
#个名为 finished_sandwiches 的空列表。遍历列表 sandwich_orders ，对于其中的每种
#三明治，都打印一条消息，如 I made your tuna sandwich ，并将其移到列表 
#finished_sandwiches 。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
#4.五香烟熏牛肉（ pastrami ）卖完了 ：使用为完成练习 7-8 而创建的列表 sandwich_orders ，
#并确保 'pastrami' 在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息
#指出熟食店的五香烟熏牛肉卖完了；再使用一个 while 循环将列表 sandwich_orders 中的
# 'pastrami' 都删除。确认最终的列表 finished_sandwiches 中不包含 'pastrami' 。

sandwich_orders = ["chicken","pastrami","pastrami","pastrami","pastrami","beef","pork"]
finished_sandwiches = []
print ("点单的三明治：")
print ( sandwich_orders )
while sandwich_orders :
    print ( "I made your tuna sandwich!")
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
print("所有的三明治已经做好！")
print(finished_sandwiches)

print ("五香烟熏牛肉售罄。")
sandwich_orders = ["chicken","pastrami","pastrami","pastrami","pastrami","beef","pork"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("结果：")
print (sandwich_orders)