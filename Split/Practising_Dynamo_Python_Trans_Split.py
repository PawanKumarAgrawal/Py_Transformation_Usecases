#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel('Downloads/Excel_sales_w04_2.xlsx')


# In[3]:


# Specify the separator(s)
separators = '|'.join(['-', ',', ';'])  # Combine separators into a regex pattern


# In[4]:


# Split the combined column based on the specified separators
df_split = df['Order_ID'].str.split(separators, expand=True)


# In[5]:


# Rename the columns if needed
df_split.columns = [f'Column{i}' for i in range(1, df_split.shape[1] + 1)]


# In[9]:


# Extract the split columns
split_columns = [df_split[col].tolist() for col in df_split.columns]


# In[12]:


df_splitted_Order_ID = pd.DataFrame(split_columns).transpose()


# In[13]:


df_splitted_Order_ID


# In[ ]:




