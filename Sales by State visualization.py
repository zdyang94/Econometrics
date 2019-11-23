#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import os
import matplotlib.pyplot as plt
import heapq
import numpy as np

sales=pd.read_csv("BBSales.csv")


# In[24]:


sales.head()


# In[32]:


data=sales.loc[:,'Kids':'Health']


# In[133]:


geo=['South',
'West',
'Southwest',
'South',
'West',
'West',
'New England',
'Middle Atlantic',
'South',
'South',
'West',
'West',
'Midwest',
'Midwest',
'Midwest',
'Midwest',
'South',
'South',
'New England',
'Middle Atlantic',
'New England',
'Midwest',
'Midwest',
'South',
'South',
'West',
'Midwest',
'West',
'New England',
'Middle Atlantic',
'Southwest',
'Middle Atlantic',
'South',
'Midwest',
'Midwest',
'Southwest',
'West',
'Middle Atlantic',
'New England',
'South',
'Midwest',
'South',
'Southwest',
'West',
'New England',
'South',
'West',
'South',
'Midwest',
'West'
]

geocol={'West':'red','East':'blue','Middle Atlantic':'yellow','South':'green','New England':'purple','Midwest':'grey','Southwest':'pink'}
geocl=[]
for i in geo:
    geocl.append(geocol[i])
    
plt.figure(figsize=(20,10))
a=plt.scatter(data['Kids'],data['Health'],s=sales['Population']/10000,alpha=0.8,c=geocl,label=sales['State'])
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.xticks([100,1000,10000,100000], ['0.1k','1k','10k','100k'])
plt.yticks([100,1000,10000,100000], ['0.1k','1k','10k','100k'])
plt.xlabel('Spending on kids',fontsize=30)
plt.ylabel('Spending on health', fontsize=30)
plt.title('Health Spending and Kid Spending by geographic distribution',fontsize=40)

plt.text(190000,650, 'West: Red ')
plt.text(190000,500,         'East: Blue')
plt.text(190000,360,         'Middle Atlantic: Yellow')
plt.text(190000,270,         'South: Green')
plt.text(190000,200,         'New England: Purple')
plt.text(190000,150,         'Midwest: Grey')
plt.text(190000,110,         'Southwest: Pink')


# In[62]:


print(geocol)


# In[ ]:




