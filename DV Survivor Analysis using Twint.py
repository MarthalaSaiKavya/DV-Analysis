#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# extract data from twitter 
import twint

##Solve compatibility issues with notebooks and RunTime errors
import nest_asyncio
nest_asyncio.apply()


# In[2]:


c= twint.Config()
c.Search= "#WhyIStayed OR #WhySheStayed"
c.Lang="en"
c.Pandas= True

twint.run.Search(c)


# In[3]:


list_ = ["#WhyIStayed","#WhySheStayed"]


# In[4]:


# Saving in dataframe

def columne_names():
  return twint.output.panda.Tweets_df.columns


# In[11]:


def twint_to_pd(columns):
  return twint.output.panda.Tweets_df[columns]


# In[12]:


data= twint_to_pd(["tweet","hashtags"])


# In[13]:


data.to_csv('DV1.csv',header=False,encoding='utf-8',index=False)


# In[14]:


import nltk


# In[15]:


len(data)

