
# coding: utf-8

# In[2]:


import numpy as np
import pandas as df


# In[3]:


data = df.read_table('ZS66BHFH014-Alignment-HitTable.csv',header=None)


# In[ ]:


np.shape(data)


# In[ ]:


val = list(data.iloc[:,0])


# In[4]:


names = []
titles = []
for item in val:
    stuff = item.split(',')
    if stuff[0] not in titles:
        titles.append(stuff[0])
        names.append(stuff[1])
        
print titles
    


# In[5]:


### this is the list of top 6 amino acids


# In[6]:



names

