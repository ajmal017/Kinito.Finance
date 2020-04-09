#!/usr/bin/env python
# coding: utf-8
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>
# # NumPy Exercises
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks and then you'll be asked some more complicated questions.
# ** IMPORTANT NOTE! Make sure you don't run the cells directly above the example output shown, otherwise you will end up writing over the example output! **
# #### Import NumPy as np
import numpy as np
# #### Create an array of 10 zeros 
np.zeros(10)
# #### Create an array of 10 ones
np.ones(10)
# #### Create an array of 10 fives
np.ones(10) * 5
# #### Create an array of the integers from 10 to 50
np.arange(10,51)
# #### Create an array of all the even integers from 10 to 50
np.arange(10,51,2)
# #### Create a 3x3 matrix with values ranging from 0 to 8
np.arange(9).reshape(3,3)
# #### Create a 3x3 identity matrix
np.eye(3)
# #### Use NumPy to generate a random number between 0 and 1
np.random.rand(1)
# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.randn(25)
# #### Create the following matrix:
np.arange(1,101).reshape(10,10) / 100
# #### Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0,1,20)
# ## Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)
mat
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[2:,1:]
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3,4]
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[:3,1:2]
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[4,:]
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3:5,:]
# ### Now do the following
# #### Get the sum of all the values in mat
mat.sum()
# #### Get the standard deviation of the values in mat
mat.std()
# #### Get the sum of all the columns in mat
mat.sum(axis=0)
# ## Bonus Question
# We worked a lot with random data with numpy, but is there a way we can insure that we always get the same random numbers? [Click Here for a Hint](https://www.google.com/search?q=numpy+random+seed&rlz=1C1CHBF_enUS747US747&oq=numpy+random+seed&aqs=chrome..69i57j69i60j0l4.2087j0j7&sourceid=chrome&ie=UTF-8)
np.random.seed(101)
# # Great Job!
