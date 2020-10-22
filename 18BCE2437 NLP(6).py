#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)


# In[3]:


print(result)


# In[4]:


result.draw()


# In[ ]:




