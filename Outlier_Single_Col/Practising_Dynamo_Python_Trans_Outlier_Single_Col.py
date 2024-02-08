#!/usr/bin/env python
# coding: utf-8

# # Handling Outliers on the Basis of Single_Col

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel('Downloads/Excel_sales_w04_2.xlsx')
df.head(3)


# In[3]:


df.info()


# In[4]:


# Function to handle outliers using IQR
def handle_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define lower and upper bounds to identify outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Round lower and upper bounds to 2 decimal places
    lower_bound_rounded = round(lower_bound, 4)
    upper_bound_rounded = round(upper_bound, 4)
    
    # Print rounded lower and upper bounds
    print("Lower Bound:", lower_bound_rounded)
    print("Upper Bound:", upper_bound_rounded)

    # Identify and handle outliers by capping them at the upper and lower bounds
    dataframe['Profit_Outlier'] = dataframe[column].apply(lambda x: f'More than Upper Bound {upper_bound_rounded}' if x > upper_bound else f'Less Than Lower Bound {lower_bound_rounded}' if x < lower_bound else x)

# Apply the IQR method to handle outliers in the 'Profit' column
handle_outliers_iqr(df, 'Profit')


# In[5]:


# Displaying the resulting table with outliers handled
df_new = df[['Profit', 'Profit_Outlier']]
df_new.head(5)


# In[ ]:





# In[ ]:




