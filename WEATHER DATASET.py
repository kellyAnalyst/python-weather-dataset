#!/usr/bin/env python
# coding: utf-8

# # The Weather Dataset 

# -Contains per hour information about weather conditions at a particular location
# -Records Temperature, Dew Point Temperature, wind speed, visibility, pressure and conditions. CSV FILE with Pandas dataframe

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\DELL\Desktop\Python tutorials\file.csv")


# In[3]:


data


# # Exploration of the Dataset

# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.index


# In[7]:


data.columns


# In[8]:


data.dtypes


# In[10]:


data['Weather'].unique()


# In[11]:


data.nunique()


# In[12]:


data.count()


# In[13]:


data['Weather'].value_counts()


# In[14]:


data.info()


# # Finding all unique 'Wind Speed' values in the data 

# In[15]:


data.head(2)


# In[16]:


data.nunique()


# In[17]:


data['Wind Speed_km/h'].nunique()


# In[18]:


data['Wind Speed_km/h'].unique()


# ## Find the number of times when the Weather is exactly clear.

# In[19]:


data.head(2)


# In[20]:


data.Weather.value_counts()


# In[21]:


data[data.Weather == 'Clear']


# In[22]:


data.groupby('Weather').get_group('Clear')


# ## Finding the number of times when the Wind speed was exactly 4km/h

# In[23]:


data.head(2)


# In[25]:


data[data['Wind Speed_km/h'] == 4]


# In[26]:


data.groupby('Wind Speed_km/h').get_group(4)


# ## finding all null values 

# In[27]:


data.head(2)


# In[29]:


data.isnull().sum()


# In[30]:


data.notnull().sum()


# ## Renaming the column weather to weather condition

# In[31]:


data.head(2)


# In[34]:


data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True)


# In[35]:


data.head(2)


# ## What is the mean Visibility?

# In[36]:


data.head(2)


# In[37]:


data.Visibility_km.mean()


# ## Standard Deviation of Pressure 

# In[38]:


data.head(2)


# In[39]:


data.Press_kPa.std()


# ## what is the variance of Relative humidity in this data 

# In[40]:


data.head(2)


# In[43]:


data['Rel Hum_%'].var()


# ## Find all instances when snow was recorded 

# In[46]:


#data.head(2)
data['Weather Condition'].value_counts()


# In[48]:


data[data['Weather Condition'] == 'Snow']


# In[53]:


data[data['Weather Condition'].str.contains('Snow')].head(50)


# ## Find all instances when wind speed is above 24 and visibility is 25

# In[54]:


data.head(2)


# In[56]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# ## What is the mean value of each column against each other weather condition

# In[57]:


data.head(2)


# In[59]:


data.groupby('Weather Condition').mean(numeric_only = True)


# ## What is the minimum & Maximum value of each column against each weather condition

# In[60]:


data.head(2)


# In[61]:


data.groupby('Weather Condition').min(numeric_only=True)


# In[63]:


data.groupby('Weather Condition').max(numeric_only=True)


# ## all records where weather condition is Fog

# In[64]:


data[data['Weather Condition'] == 'Fog']


# ## Find all instances when weather is clear or visibility is above 40

# In[66]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# ### A= Weather is clear and relative humidity is greater than 50
# 
# ### OR
# 
# ### B= Visibility is above 40
# 

# In[67]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50 ) | (data['Visibility_km'] > 40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




