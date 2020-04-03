#!/usr/bin/env python
# coding: utf-8

# ## Estimating the Sharpe Ratio in Python

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Load the data for Microsoft and S&P 500 for the period 1st of January 2012 – 31st of December 2016. 
# Let S&P 500 act as the market. 
# Calculate the beta of Microsoft. <br />
# 
# Assume a risk-free rate of 2.5% and a risk premium of 5%.<br />
# Estimate the expected return of Microsoft.
# 
# 

# In[ ]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb

data = pd.read_csv('D:\Python\CAPM_Exercise_Data.csv', index_col = 'Date')
data
    
sec_returns = np.log( data / data.shift(1) )
cov = sec_returns.cov() * 250
cov_with_market = cov.iloc[0,1]
market_var = sec_returns['^GSPC'].var() * 250

MSFT_beta = cov_with_market / market_var
MSFT_er = 0.025 + MSFT_beta * 0.05


# Calculate the Sharpe ratio in Python.

# **Sharpe ratio:**
# ### $$
# Sharpe = \frac{\overline{r_{pg}} - r_f}{\sigma_{pg}}
# $$

# In[ ]:



