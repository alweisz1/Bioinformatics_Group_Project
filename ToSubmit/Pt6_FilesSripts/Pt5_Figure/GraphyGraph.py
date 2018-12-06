
# coding: utf-8

# In[37]:


import numpy as np
import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt


# In[38]:


data1 = pd.read_csv("TabulatedValControl1protein.csv")
data2 = pd.read_csv("TabulatedValControl2protein.csv")
data3 = pd.read_csv("TabulatedValObese1protein.csv")
data4 = pd.read_csv("TabulatedValObese2protein.csv")


# In[45]:


data1a = data1.loc[0::2].astype(int)
data2a = data2.loc[0::2].astype(int)
data3a = data3.loc[0::2].astype(int)
data4a = data4.loc[0::2].astype(int)


# In[44]:


# data to plot
import matplotlib.pyplot as plt
n_groups = 6
Ctrl1 = (data1a.iloc[0,0],data1a.iloc[1,0],data1a.iloc[2,0],data1a.iloc[3,0],data1a.iloc[4,0],data1a.iloc[5,0])
Ctrl2 = (data2a.iloc[0,0],data2a.iloc[1,0],data2a.iloc[2,0],data2a.iloc[3,0],data2a.iloc[4,0],data2a.iloc[5,0])
Obese1 = (data3a.iloc[0,0],data3a.iloc[1,0],data3a.iloc[2,0],data3a.iloc[3,0],data3a.iloc[4,0],data3a.iloc[5,0])
Obese2 = (data4a.iloc[0,0],data4a.iloc[1,0],data4a.iloc[2,0],data4a.iloc[3,0],data4a.iloc[4,0],data4a.iloc[5,0])

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.175
opacity = 0.8

print type(index)
rects1 = plt.bar(index, Ctrl1, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Control1')
 
rects2 = plt.bar(index + bar_width, Ctrl2, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Control2')

rects3 = plt.bar(index + 2*bar_width, Obese1, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Obese1')
rects4 = plt.bar(index + 3*bar_width, Obese2, bar_width,
                 alpha=opacity,
                 color='k',
                 label='Obese2')
 
plt.xlabel('Experiment')
#plt.ylim(0,20)
plt.ylabel('# Hits')
plt.title('Expression Ratio in Obese vs non-Obese Mice')
plt.xticks(index + bar_width, ('Sequence10', 'Sequence1', 'Sequence2', 'Sequence6','Sequence8','Sequence9'))
plt.legend()
 
plt.tight_layout()
plt.show()


# In[41]:




