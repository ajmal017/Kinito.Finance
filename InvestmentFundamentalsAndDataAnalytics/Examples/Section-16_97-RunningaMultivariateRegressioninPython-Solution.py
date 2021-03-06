#!/usr/bin/env python
# coding: utf-8
## Running a Multivariate Regression in Python
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Let’s continue working on the file we used when we worked on univariate regressions.
# *****
# Run a multivariate regression with 5 independent variables – from Test 1 to Test 5.
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt
data = pd.read_excel('Section-13_IQ_data.xlsx')
data.head()
# ### Multivariate Regression:
# Independent Variables: *Test 1, Test 2, Test 3, Test 4, Test 5*
# In[4]:
X = data[['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']]
X = data.iloc[:,[1,2,3,4,5]]
Y = data.iloc[:,0]
# In[5]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# The p-value of the variable Test 1 in the univariate regression looked very promising. Is it still low? If not – what do you think would be the reason for the change?
# Try regressing Test 1 and Test 2 on the IQ score first. Then, regress Test 1, 2, and 3 on IQ, and finally, regress Test 1, 2, 3, and 4 on IQ. What is the Test 1 p-value in these regressions?
# Independent Variables: *Test 1, Test 2*
# In[6]:
X = data[['Test 1', 'Test 2']]
X = data.iloc[:,[1,2]]
Y = data.iloc[:,0]
# In[7]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *Test 1, Test 2, Test 3*
# In[8]:
X = data[['Test 1', 'Test 2', 'Test 3']]
X = data.iloc[:,[1,2,3]]
Y = data.iloc[:,0]
# In[9]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *Test 1, Test 2, Test 3, Test 4*
# In[10]:
X = data[['Test 1', 'Test 2', 'Test 3', 'Test 4']]
X = data.iloc[:,[1,2,3,4]]
Y = data.iloc[:,0]
# In[11]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# It seems it increases a lot when we add the result from Test 4. 
# ****
# Run a regression with only Test 1 and Test 4 as independent variables. How would you interpret the p-values in this case?
# Independent Variables: *Test 1, Test 4*
# In[12]:
X = data[['Test 1', 'Test 4']]
X = data.iloc[:,[1,4]]
Y = data.iloc[:,0]
# In[13]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *Test 4*
# In[14]:
X = data[['Test 4']]
X = data.iloc[:,4]
Y = data.iloc[:,0]
# In[15]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# ***Suggested Answer:***
# *Test 1 and Test 4 are correlated, and they contribute to the preparation of the IQ test in a similar way.*
