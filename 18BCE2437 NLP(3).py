#!/usr/bin/env python
# coding: utf-8

# In[4]:


#TASK 1: BACSIC TEXT PROCESSING PIPELINE
import nltk
text1 = '''Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS.
Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.
Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.
Visual Studio Code's source code comes from Microsoft's free and open-source software VSCode project released under the permissive Expat License, but the compiled binaries are freeware for any use.'''

for text in text1:
    sentences=nltk.sent_tokenize(text1)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        tagged=nltk.pos_tag(words)
        print(tagged)


# In[6]:


#TASK 2: TweetTokenizer
from nltk.tokenize import TweetTokenizer
text= 'We are going to WIN the 2020 Election, BIG! #MAGA'
twtkn= TweetTokenizer()
twtkn.tokenize(text)


# In[7]:


#TASK 3: SCRAPING DATA FROM WEB
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw= response.read().decode('utf8')
type(raw)
len(raw)
raw[:75]
from nltk.tokenize import word_tokenize
tokens=word_tokenize(raw)
type(tokens)
#HTML => ASCII => TEXT => VOCAB


# In[11]:


#TASK 4. HANDLING TWEETS DATA
import nltk
f = open('tweets1.txt','r')
text=f.read()
text1=text.split()
text2=nltk.Text(text1)
text2.concordance("good")


# In[ ]:





# In[ ]:





# In[ ]:




