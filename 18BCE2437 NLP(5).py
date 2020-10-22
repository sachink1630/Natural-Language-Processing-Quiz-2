#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 2 SIMPLE TEXT CLASSIFICATION
def gender_features(word):
    return {'last_letter':word[-1]}


# In[2]:


gender_features('Obama')


# In[10]:


names.words()


# In[6]:


nltk.download('names')


# In[8]:


import nltk


# In[9]:


nltk.download('names')


# In[11]:


#TASK 3 COUNT VECTORIZER
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(binary=True)
corpus = ["Tessaract is good optical character recognition engine  ", "optical character recognition is significant "]


# In[ ]:




