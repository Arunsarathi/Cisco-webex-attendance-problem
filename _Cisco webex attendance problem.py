#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# step-1
# save as attendance.csv to attendance.xlsx


# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df1 = pd.read_excel('attendance.xlsx')
df1.head()


# In[ ]:


print('no. of name-duplicated',df2.Name.duplicated().sum())

print('no. of Email-duplicated',df2.Email.duplicated().sum())


# In[ ]:


df2=df1[['Name', 'Email','Duration']]
df2['Duration']=df2['Duration'].str.replace("mins","")
df2['Duration']=df2['Duration'].str.replace("min","")
df2['Duration']=df2['Duration'].astype(int)
dff=df2.copy()
df2.drop_duplicates(subset=['Email'])
dff=df2.copy()
df8=df2.groupby('Email').agg({'Duration': 'sum', 'Name': lambda x: '//'.join(x)})
df8['Name']=df8.Name.str.split("//").str.get(0)
df8.to_excel("out.xlsx") 
df9 = pd.read_excel('out.xlsx')
df9=df9[['Name','Email','Duration']].copy()
df9.sort_values(["Duration"], axis=0, 
                 ascending=True, inplace=True) 
df9.head()


# In[ ]:


df9.to_excel("FDP_Day_1.xlsx") 

