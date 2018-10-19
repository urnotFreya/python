# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:43:22 2018

@author: Administrator
"""

import numpy as np 
#随机梯度算法
#假设x的值
X=[[2104,3],[1600,3],[2400,3],[1416,2],[3000,4]]
Y=[[400,330,369,232,540]]
learning_rate=0.001
epsilon=0.0001
iters=10000
count=0
theta=[0,0,0]
h=[]
while count<iters:
    for i in range(len(X)):
        hs=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]
        h.append(hs)
        for j in range(len(theta)):
            print (str(i)+"  "+str(j))
            o=X[i][j]
            print (o)
#            theta[j]=theta[j]+learning_rate*(y[i]-h[i])*X[i][j]
        error=abs(Y[i]-hs)
        if error<epsilon:
            break
        iters=iters+1
print (theta)         
"""

# 训练集  
# 每个样本点有3个分量 (x0,x1,x2)  
x = [(1, 0., 3), (1, 1., 3), (1, 2., 3), (1, 3., 2), (1, 4., 4)]  
# y[i] 样本点对应的输出  
y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]  
  
# 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代  
epsilon = 0.0001  
  
# 学习率  
alpha = 0.01  
diff = [0, 0]  
max_itor = 1000  
error1 = 0  
error0 = 0  
cnt = 0  
m = len(x)  
  
  
# 初始化参数  
theta0 = 0  
theta1 = 0  
theta2 = 0  
  
while True:  
    cnt += 1  
  
    # 参数迭代计算  
    for i in range(m):  
        # 拟合函数为 y = theta0 * x[0] + theta1 * x[1] +theta2 * x[2]  
        # 计算残差  
        diff[0] = (theta0 + theta1 * x[i][1] + theta2 * x[i][2]) - y[i]  
  
        # 梯度 = diff[0] * x[i][j]  
        theta0 -= alpha * diff[0] * x[i][0]  
        theta1 -= alpha * diff[0] * x[i][1]  
        theta2 -= alpha * diff[0] * x[i][2]  
  
    # 计算损失函数  
    error1 = 0  
    for lp in range(len(x)):  
        error1 += (y[lp]-(theta0 + theta1 * x[lp][1] + theta2 * x[lp][2]))**2/2  
  
    if abs(error1-error0) < epsilon:  
        break  
    else:  
        error0 = error1  
  
    print (' theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f' % (theta0, theta1, theta2, error1))  
print ('Done: theta0 : %f, theta1 : %f, theta2 : %f' % (theta0, theta1, theta2))  
print ('迭代次数: %d' % cnt)  
"""