#!/usr/bin/env python
# coding: utf-8

# # Explore descriptive statistics

# ## **Introduction**
# 
# Data professionals often use descriptive statistics to understand the data they are working with and provide collaborators with a summary of the relative location of values in the data, as well an information about its spread. 
# 
# For this activity, you are a member of an analytics team for the United States Environmental Protection Agency (EPA). You are assigned to analyze data on air quality with respect to carbon monoxide, a major air pollutant. The data includes information from more than 200 sites, identified by state, county, city, and local site names. You will use Python functions to gather statistics about air quality, then share insights with stakeholders.

# ## **Step 1: Imports** 
# 

# Import the relevant Python libraries `pandas` and `numpy`.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# The dataset provided is in the form of a .csv file named `c4_epa_air_quality.csv`. It contains a subset of data from the U.S. EPA. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[22]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE
epa_data = pd.read_csv("c4_epa_air_quality.csv", index_col = 0)


# ## **Step 2: Data exploration** 

# To understand how the dataset is structured, display the first 10 rows of the data.

# In[8]:


# Display first 10 rows of the data.
epa_data.head(10)


# **Question:** What does the `aqi` column represent?

# “Air Quality Index” – AQI is like a thermometer that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern.

# Now, get a table that contains some descriptive statistics about the data.

# In[9]:


# Get descriptive stats.
epa_data.describe()


# **Question:** Based on the table of descriptive statistics, what do you notice about the count value for the `aqi` column?

# There are 260 observations.

# **Question:** What do you notice about the 25th percentile for the `aqi` column?
# 
# This is an important measure for understanding where the aqi values lie. 

# The 25% of the readings of AQI are below or equal 2, meaning that there are not health concerns.

# **Question:** What do you notice about the 75th percentile for the `aqi` column?
# 
# This is another important measure for understanding where the aqi values lie. 

# The 75% of the readings of AQI are below or equal to 9, meaning that there are not health concerns.

# ## **Step 3: Statistical tests** 

# Next, get some descriptive statistics about the states in the data.

# In[10]:


# Get descriptive stats about the states in the data.
epa_data['state_name'].describe()


# **Question:** What do you notice while reviewing the descriptive statistics about the states in the data? 
# 
# Note: Sometimes you have to individually calculate statistics. To review to that approach, use the `numpy` library to calculate each of the main statistics in the preceding table for the `aqi` column.

# There are 260 observations, with 52 unique states, from them California is the one thats is repeated the most 66 times.

# ## **Step 4. Results and evaluation**

# Now, compute the mean value from the `aqi` column.

# In[12]:


# Compute the mean value from the aqi column.

round(np.mean(epa_data['aqi']),2)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about descriptive statistics in Python.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
#   There is a function in the `numpy` library that allows you to get the mean value from an array or a Series of values.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
#   Use the `mean()` function from the `numpy` library.
# 
# </details>

# **Question:** What do you notice about the mean value from the `aqi` column?
# 
# This is an important measure, as it tells you what the average air quality is based on the data.

# The mean of the aqi index is 6.76. 

# Next, compute the median value from the aqi column.

# In[13]:


# Compute the median value from the aqi column.

np.median(epa_data['aqi'])


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to the video about descriptive statistics in Python.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
#   There is a function in the `numpy` library that allows you to get the median value from an array or a series of values.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
#   Use the `median()` function from the `numpy` library.
# 
# </details>

# **Question:** What do you notice about the median value from the `aqi` column?
# 
# This is an important measure for understanding the central location of the data.

# The half of the meaure are below 5.0, meaning that half of them are below the mean. This can mean that the are some high values that affect the mean. 

# Next, identify the minimum value from the `aqi` column.

# In[15]:


# Identify the minimum value from the aqi column.

np.min(epa_data['aqi'])


# **Question:** What do you notice about the minimum value from the `aqi` column?
# 
# This is an important measure, as it tell you the best air quality observed in the data.

# The minimum is zero, indicating that there are some readings where the state had an AQI index of 0.

# Now, identify the maximum value from the `aqi` column.

# In[16]:


# Identify the maximum value from the aqi column.

np.max(epa_data['aqi'])


# **Question:** What do you notice about the maximum value from the `aqi` column?
# 
# This is an important measure, as it tells you which value in the data corresponds to the worst air quality observed in the data.

# The maximum value for the aqi column is 50. This means that the largest aqi value in the data is 50.

# Now, compute the standard deviation for the `aqi` column.
# 
# By default, the `numpy` library uses 0 as the Delta Degrees of Freedom, while `pandas` library uses 1. To get the same value for standard deviation using either library, specify the `ddof` parameter to 1 when calculating standard deviation.

# In[21]:


# Compute the standard deviation for the aqi column.

np.std(epa_data['aqi'], ddof=1)


# **Question:** What do you notice about the standard deviation for the `aqi` column? 
# 
# This is an important measure of how spread out the aqi values are.

# The standard deviation for the aqi column is approximately 7.05 (rounding to 2 decimal places here). This is a measure of how spread out the aqi values are in the data.

# ## **Considerations**
# 

# **What are some key takeaways that you learned during this lab?**

# Functions in the pandas and numpy libraries can be used to find statistics that describe a dataset. The describe() function from pandas generates a table of descriptive statistics about numerical or categorical columns. The mean(), median(), min(), max(), and std() functions from numpy are useful for finding individual statistics about numerical data.

# **How would you present your findings from this lab to others? Consider the following relevant points noted by AirNow.gov as you respond:**
# - "AQI values at or below 100 are generally thought of as satisfactory. When AQI values are above 100, air quality is considered to be unhealthy—at first for certain sensitive groups of people, then for everyone as AQI values increase."
# - "An AQI of 100 for carbon monoxide corresponds to a level of 9.4 parts per million."

# The average AQI value in the data is approximately 6.76, which is considered safe with respect to carbon monoxide. Further, 75% of the AQI values are below 9.
# 
# 

# **What summary would you provide to stakeholders? Use the same information provided previously from AirNow.gov as you respond.**

# 75% of the AQI values in the data are below 9, which is considered good air quality.
# Funding should be allocated for further investigation of the less healthy regions in order to learn how to improve the conditions.
