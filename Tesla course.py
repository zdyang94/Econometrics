#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:



tesla=pd.read_csv('D:\google download\TSLA.CSV')
a=tesla.columns
print(a[1])


# In[3]:


required_data=tesla.tail(n=1000)
Variance=(required_data['Adj Close']-required_data['Open'])/required_data['Open']
required_data.insert(7,'Variance',Variance)


# In[4]:


mean=np.mean(required_data['Variance'])
mean
std=np.std(required_data['Variance'])
std


# In[5]:


required_data.dtypes
pd.set_option('mode.chained_assignment', None)


# In[6]:


required_data['Date'] = pd.to_datetime(required_data['Date'])


# In[7]:


required_data.dtypes


# In[8]:


required_data.set_index('Date',inplace=True)


# In[9]:


plt.figure(figsize=(20,6))
required_data['Adj Close'].plot()


# In[10]:


plt.figure(figsize=(20,6))
required_data['Variance'].plot(kind='kde')
required_data['Variance'].hist(bins=200,alpha=0.3,color='k',density =True)


# In[11]:


ford=pd.read_csv('D:\google download\FOR.CSV')


# In[12]:


compare=ford.tail(1000)
comVariance=(compare['Adj Close']-compare['Open'])/compare['Open']
compare.insert(7,'comVariance',comVariance)
compare['Date'] = pd.to_datetime(compare['Date'])


# In[ ]:





# In[13]:


compare.dtypes

compare.set_index('Date',inplace=True)


# In[ ]:





# In[14]:


plt.figure(figsize=(20,6))

compare['Adj Close'].plot()


# In[15]:


plt.figure(figsize=(20,6))
required_data['Adj Close'].plot()
compare['Adj Close'].plot()


# In[16]:


#not beautifle enough, and not clear to see the variance between two


# In[17]:


#create a sub-ray


# In[18]:


plt.figure(figsize=(20,6))
required_data['Adj Close'].plot()
plt.twinx()
compare['Adj Close'].plot(color='r')


# In[19]:


# Perform the KS Test to see whether Tesla's variance is normaly distributed


# In[20]:


tesla_KS=required_data.copy()


# In[21]:


ini=0
bctual=[]
for i in range(1000):
    ini+=round(1/1000,3)
    ini=round(ini,3)
    bctual.append(ini)
    


# In[22]:


tesla_KS=tesla_KS.sort_values(by= 'Variance',ascending=True)
tesla_KS.head()


# In[23]:


tesla_KS.insert(7,'Actual Prob',bctual)


# In[24]:


plt.figure(figsize=(20,6))
compare['Adj Close'].plot(color='r')


# In[25]:


tesla_KS.head()
import math
def normalcdf(X):
    '''
    calculate Cumulative Distribution Function，CDF  got from internet
    '''
    T=1/(1+.2316419*abs(X))
    D=0.3989423*math.exp(-X*X/2)
    Prob=D*T*(0.3193815+T*(-0.3565638+T*(1.781478+T*(-1.821256+T*1.330274))))
    if X>0:
        return 1-Prob
    else:
        return Prob
    
#make a wrapping
def normalize(x):
    n=[]
    for i in x:
        n.append(normalcdf(i))
    return n

tesla_KS['Zscore'] = (tesla_KS['Variance'] - mean)/std
print(normalcdf(-3.471790))

tesla_KS['Theo Prob']=normalize(tesla_KS['Zscore'])
tesla_KS.head()


# In[26]:


tesla_KS['Abs Diff']=abs(tesla_KS['Actual Prob']-tesla_KS['Theo Prob'])


# In[27]:


tesla_KS.head()


# In[28]:


maxdif=max(tesla_KS['Abs Diff'])
print(maxdif)


# Therefore, the last step is to compare the maximum absolute difference against the table value
# 1000 obs
# 95% confidence interval
# look up the critical value in KS table
# ks=1.36/(1000)^0.5=0.043007
# Conclusion: the variance of Tesla is comply with normal distribution!

# According to the textbook, since the example failed in the KS test, then performed a 1 tail test， just try to do it right now

# In[29]:


# 1. sort the original tabel into 10 groups
tesla_BS=required_data.copy()
tesla_BS.head()


# In[30]:


mean_bs=[]
variance_bs=[]
for i in range(10):
    mean_bs.append(np.mean(tesla_BS['Variance'][i:i+10]))
    variance_bs.append(np.std(tesla_BS['Variance'][i:i+10]))
print(mean_bs)
print(variance_bs)
        


# In[31]:


BS=pd.DataFrame({"Mean":mean_bs,"Variance":variance_bs})


# In[32]:


print(BS)


# In[33]:


from_bs=[]
to_bs=[]
for i in range(10):
    from_bs.append(i*100+1)
    to_bs.append(i*100+100)


# In[34]:


BS['From']=from_bs
BS['To']=to_bs

print(BS)


# In[35]:


max_mean=max(BS['Mean'])
max_var=max(BS['Variance'])
min_mean=min(BS['Mean'])
min_var=min(BS['Variance'])


# In[36]:


test_statistic=(max_mean-min_mean)/(math.sqrt(max_var/100+min_var/100))


# In[37]:


print(test_statistic)


# look up the critical value for 1 tail T test, 95% confidence interval:
# degree of freedom=100+100-2=198
# t value =1.653
# therefore, we can conclude that the two sample tested are coming from the same distribution.

# In[ ]:





# In[ ]:




