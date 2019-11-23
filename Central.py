# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:49:09 2019

@author: Allen
"""

import numpy as np
import matplotlib.pyplot as plt

epsilon=0.1
X1=np.random.normal(5,2,50).astype(np.float32)
X2=np.random.normal(12,2,50).astype(np.float32)
x=np.array([X1,X2])
Y1=np.random.normal(3,2,50).astype(np.float32)
Y2=np.random.normal(9,2,50).astype(np.float32)
y=np.array([Y1,Y2])
k=2
#plt.scatter(x,y)
oricentriods=[[5,4],[12,10]]
newx1=[]
newy1=[]
newx2=[]
newy2=[]

record=[]
Flag=False

for n in range(2000):
    clustera=[]
    clusterb=[]
    for i in range(2):
        for j in range(50):


            if (x[i][j]-oricentriods[0][0])**2+(y[i][j]-oricentriods[0][1])**2>(x[i][j]-oricentriods[1][0])**2+(y[i][j]-oricentriods[1][1]):
                clusterb.append((x[i][j],y[i][j]))

            else:
                clustera.append((x[i][j],y[i][j]))
    record=oricentriods.copy()
    x1=0
    y1=0
    for i in range(len(clustera)):
        x1+=clustera[i][0]
        y1+=clustera[i][1]
    x1=x1/len(clustera)
    y1=y1/len(clustera)
    
    x2=0
    y2=0
    for i in range(len(clusterb)):
        x2+=clusterb[i][0]
        y2+=clusterb[i][1]
    x2=x2/len(clustera)
    y2=y2/len(clustera)
    oricentriods=[[x1,y1],[x2,y2]]
    
for i in range(2):
    for j in range(50):
        if (x[i][j]-oricentriods[0][0])**2+(y[i][j]-oricentriods[0][1])**2>(x[i][j]-oricentriods[1][0])**2+(y[i][j]-oricentriods[1][1]):
            clusterb.append((x[i][j],y[i][j]))
        else:
            clustera.append((x[i][j],y[i][j]))

plt.figure(figsize=(6,3.5))
plt.grid()
for i in range(len(clustera)):
    plt.scatter(clustera[i][0],clustera[i][1],color='coral',alpha=0.6)
for i in range(len(clusterb)):
    plt.scatter(clusterb[i][0],clusterb[i][1],color='steelblue',alpha=0.6)
plt.scatter(oricentriods[0][0],oricentriods[0][1],s=500,color='coral',edgecolors='black')
plt.scatter(oricentriods[1][0],oricentriods[1][1],s=500,color='steelblue',edgecolors='black')
plt.xlabel('Petal length(cm)')
plt.ylabel('Petal witdth(cm)')
plt.title('K-Means Algorithm -k=2 - Iteration 2')
