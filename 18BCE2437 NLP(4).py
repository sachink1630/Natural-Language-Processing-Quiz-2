#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('inaugural')


# In[2]:


from nltk.corpus import inaugural
print(inaugural.fileids(),'\n\n')


# In[3]:


FileName= '1789-Washington.txt'


# In[4]:


print(inaugural.words(fileids=FileName)[:10])


# In[5]:


Text = ' '.join(inaugural.words(fileids=FileName))
Text


# In[6]:


FrequencyDistribution=nltk.FreqDist(inaugural.words(fileids=FileName))
FrequencyDistribution


# In[7]:


from nltk.probability import ConditionalFreqDist


# In[8]:


CFD=ConditionalFreqDist((len(word),word) for word in inaugural.words(fileids=FileName))
CFD[5]


# In[9]:


get_ipython().system(' pip install wordcloud')


# In[10]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 


# In[11]:


wordcloud = WordCloud(width=1280, height=720,relative_scaling = 1.0,stopwords = STOPWORDS).generate(Text)
plt.savefig("WordCloud.png")
plt.figure(figsize=(15,15))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()


# In[ ]:




