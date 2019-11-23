#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy import stats
import math
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols


# In[43]:


data=pd.read_csv('Original Data.csv')


# In[44]:


# since the data is not in perfect form, I need to extract the "day" information for further information
def transferdate(d):
    for i in range(len(d)):
        if d[i]=='-':
            break
    return int(d[:i])


# In[45]:


date=data['Date'] #extract date from data
day=list(map(transferdate,date))
data['Days']=day #add back to data


# In[46]:


#create a tool to remove %

def remove(a):
    return float(a[:-1])/100
#create a tool to calculate mean
def mean(a):
    n=0
    for i in a:
        n+=i
    return n/len(a)
#create a tool to calculate sita

    


# In[47]:


#create a filtering tool to seperate the data into beginning and after month
def judgedate(n):
    if n <11:
        return 1
    elif n > 19:
        return 2
    else:
        return 0
filt=list(map(judgedate,data['Days']))
data['Filt']=filt




begofmonth=data[data.Filt==1]
endofmonth=data[data.Filt==2]
begdata=list(map(remove,begofmonth['Stock Return']))
enddata=list(map(remove,endofmonth['Stock Return']))
t2, p2 = stats.ttest_ind(begdata,enddata)

nb=len(begofmonth.iloc[:,0])
ne=len(endofmonth.iloc[:,0])
ub=sum(list(map(remove,begofmonth['Stock Return'])))/nb
ue=sum(list(map(remove,endofmonth['Stock Return'])))/ne

varb=np.var(list((map(remove,begofmonth['Stock Return']))))
vare=np.var(list((map(remove,endofmonth['Stock Return']))))

t=(ub-ue)/(np.sqrt(varb/nb+vare/ne))
dof=nb+ne-2
cr=stats.t.ppf(0.975,df=dof)
if abs(t2) < cr:
    print('Cannot reject Null hypothesis that u1=u2')
else:
    print('can reject null hypothesis, u1!=u2')


# In[49]:


#conduct F test
#f.ppf(0.01, dfn, dfd)
Fr=stats.f.ppf(0.95,nb,ne)
ftest=varb/vare
if ftest<1:
    ftest=1/ftest
if ftest < Fr:
    print('Cannot reject Null hypothesis that std1=std2')
else:
    print('can reject null hypothesis, std1!=std2')


# In[50]:


# Next step is to do the GQ Test
# Model: Ln(St)=Ln(S0)+r*T+et
# 1st step is to convert the data in the target form


# In[56]:


##create the x variable, date
def adddate(a):
    day=[]
    for i in range(len(a.iloc[:,0])):
        day.append(i+1)
    a.loc[:,'Daynum']=day
    return a
GQ_Beg=adddate(begofmonth)
GQ_End=adddate(endofmonth)
GQ_Total=adddate(data)


# In[52]:


#set Y value in the regression, which is ln(100*(1+return))

def addY(a):
    fin=[]
    ret=(list(map(remove,a['Stock Return'])))
    res=[]
    for i in range(len(ret)):
        if i==0:
            res.append((1+ret[i])*100)
        else:
            res.append((1+ret[i])*res[i-1])
    
    for i in res:
        fin.append(np.log(i))

    a['Price']=res
    a['Y']=fin
    return a


# In[63]:


def getsse(a):
    a=addY(a)

    x=[x for x in a.loc[:,'Daynum']]
    y=[y for y in a.loc[:,'Y']]

    d=sm.OLS(y,x).fit()
    regressor = LinearRegression()
    regressor.fit(a[['Daynum']],a[['Y']])

    coef=regressor.coef_

    inter=regressor.intercept_
    pred=x*coef+inter
    t=(y-pred)**2
    SSE=np.sum(t)
    return SSE


# In[64]:


#finally we need to calculate the Chow result, which can be compared with a F test.
SSEBeg=getsse(GQ_Beg)
SSEEnd=getsse(GQ_End)
SSETotal=getsse(data)
Chow=((SSETotal-SSEBeg-SSEEnd)/2)/((SSEBeg+SSEEnd)/(len(GQ_Beg)-2+len(GQ_End)-2))
print(Chow)
Fr2=stats.f.ppf(0.95,len(GQ_Beg)-2,len(GQ_End)-2)
print(Fr2)
if Chow>Fr2:
    print('Chow Test show that there is structural change')
else:
    print('Chow Test show that there is no structural change')

