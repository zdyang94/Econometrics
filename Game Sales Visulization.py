#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
game=pd.read_csv('vgsales.csv')
game.head()


# In[12]:


genbynumber={}
for i in range(16598):
    if game.iloc[i][4] in genbynumber.keys():
        genbynumber[game.iloc[i][4]]+=1
    else:
        genbynumber[game.iloc[i][4]]=1
genbysales={}
for i in range(16598):
    if game.iloc[i][4] in genbysales.keys():
        genbysales[game.iloc[i][4]]+=round(game.iloc[i][10])
    else:
        genbysales[game.iloc[i][4]]=round(game.iloc[i][10])
a=genbynumber.keys()
b=genbynumber.values()
c=genbysales.keys()
d=genbysales.values()

fig, axs = plt.subplots(1, 2, figsize=(12,6), sharey=True)
axs[0].pie(b,labels=a,autopct='%1.1f%%')
axs[0].set_title('Game type by release number')
axs[1].pie(d,labels=c,autopct='%1.1f%%')
axs[1].set_title('Game type by global sales')
plt.show()


# In[13]:


max_game=game.sort_values(by='Global_Sales',ascending=False).head(10)
max_game


# In[15]:



publisher=game['Publisher'].drop_duplicates()
game=game.dropna(axis=0,how='any')
L=len(game['Name'])
# I decided to see the sales amount of each publisher from 2000 to 2016
Y=[]
Y_n=[]
for i in range(2000,2011):
    Y.append(i)
    Y_n.append(0)


publisher_dict={}

for i in publisher:
    publisher_dict[i]=Y_n.copy()
for i in range(L):
    if game.iloc[i][3]>=2000 and game.iloc[i][3]<2011 :
        publisher_dict[game.iloc[i][5]][int(game.iloc[i][3]-2000)]+=game.iloc[i][10]
enddict=pd.DataFrame(publisher_dict)
enddict=enddict.T
enddict.columns=Y
enddict['Total Sales']=enddict.apply(lambda x: x.sum(), axis=1)


enddict=enddict.sort_values(by='Total Sales',ascending=False)
finallist=enddict.head(10)
plt.figure(figsize=(30,20))
z=np.array(Y)
width=0.1

for i in range(10):
    plt.bar(z+i*width,finallist.iloc[i][:-1],width=width, label=finallist._stat_axis.values.tolist()[i])
plt.legend(prop = {'size':20})

