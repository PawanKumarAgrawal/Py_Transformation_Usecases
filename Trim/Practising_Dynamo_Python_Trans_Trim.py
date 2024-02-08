#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df_trim = pd.read_excel('Duplicates.xlsx')
df_trim.head(3)


# In[10]:


df_trim['Name'] = df_trim['Name'].str.strip()


# In[11]:


df_trim.head(3)


# In[5]:


# Save the DataFrame as an Excel file
df_trim.to_excel('df_trim.xlsx', index=False)

print("DataFrame saved as df_trim.xlsx")


# In[ ]:




