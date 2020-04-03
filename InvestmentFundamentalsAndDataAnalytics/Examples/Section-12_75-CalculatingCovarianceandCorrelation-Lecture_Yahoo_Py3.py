#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


# In[3]:


sec_data.tail()


# In[4]:


sec_returns = np.log(sec_data / sec_data.shift(1))


# In[5]:


sec_returns


# ## PG

# In[6]:


sec_returns['PG'].mean()


# In[7]:


sec_returns['PG'].mean() * 250


# In[8]:


sec_returns['PG'].std()


# In[9]:


sec_returns['PG'].std() * 250 ** 0.5


# ## Beiersdorf

# In[10]:


sec_returns['BEI.DE'].mean()


# In[11]:


sec_returns['BEI.DE'].mean() * 250


# In[12]:


sec_returns['BEI.DE'].std()


# In[13]:


sec_returns['BEI.DE'].std() * 250 ** 0.5


# ***

# In[14]:


print (sec_returns['PG'].mean() * 250)
print (sec_returns['BEI.DE'].mean() * 250)


# In[15]:


sec_returns['PG', 'BEI.DE'].mean() * 250


# In[16]:


sec_returns[['PG', 'BEI.DE']].mean() * 250


# In[17]:


sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5


# ## Covariance and Correlation

# 
# \begin{eqnarray*}
# Covariance Matrix: \  \   
# \Sigma = \begin{bmatrix}
#         \sigma_{1}^2 \ \sigma_{12} \ \dots \ \sigma_{1I} \\
#         \sigma_{21} \ \sigma_{2}^2 \ \dots \ \sigma_{2I} \\
#         \vdots \ \vdots \ \ddots \ \vdots \\
#         \sigma_{I1} \ \sigma_{I2} \ \dots \ \sigma_{I}^2
#     \end{bmatrix}
# \end{eqnarray*}

# In[18]:


PG_var = sec_returns['PG'].var() 
PG_var


# In[19]:


BEI_var = sec_returns['BEI.DE'].var() 
BEI_var


# In[20]:


PG_var_a = sec_returns['PG'].var() * 250
PG_var_a


# In[21]:


BEI_var_a = sec_returns['BEI.DE'].var() * 250
BEI_var_a


# ***

# In[22]:


cov_matrix = sec_returns.cov()
cov_matrix


# In[23]:


cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a


# ***

# In[24]:


corr_matrix = sec_returns.corr()
corr_matrix
