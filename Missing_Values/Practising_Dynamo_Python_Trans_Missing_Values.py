#!/usr/bin/env python
# coding: utf-8

# # Handling Outliers on the Basis of Single_Col

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel('Excel_sales_w04_2.xlsx')
df.head(5)


# In[3]:


df.info()


# In[4]:


# Handling Missing Values in Sales Column
df['Sales'] = df['Sales'].fillna(0)
df.head(5)


# In[5]:


df.info()


# In[ ]:




