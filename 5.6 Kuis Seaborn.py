#!/usr/bin/env python
# coding: utf-8

# # KUIS SEABORN

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


titanic = sns.load_dataset('titanic')
titanic.head()


# ### Soal 1
# 
# Buatlah joint plot dari data di atas yang hasilnya seperti di bawah ini

# In[4]:


sns.jointplot(x='fare', y='age', data=titanic)


# ### Soal 2
# 
# Buatlah Dist plot dari data di atas dengan ketentuan:
# - bins nya 30
# - kde nya false
# - color merah
# 
# yang hasilnya seperti di bawah ini

# In[5]:


sns.distplot(titanic['fare'], bins=30, kde=False, color='red')


# ### Soal 3
# 
# Buatlah box plot dari data di atas berwarna rainbow yang hasilnya seperti di bawah ini

# In[6]:


sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')


# ### Soal 4
# 
# Buatlah swarm plot dari data di atas berwarna rainbow yang hasilnya seperti di bawah ini

# In[7]:


sns.swarmplot(x='class', y='age', data=titanic, palette='rainbow')


# ### Soal 5
# 
# Buatlah count plot dari data di atas yang hasilnya seperti di bawah ini

# In[8]:


sns.countplot(x='sex', data=titanic)


# ### Soal 6
# 
# Buatlah Heatmap dari data di atas, berwarna coolwarm, title soal 6 yang hasilnya seperti di bawah ini

# In[9]:


sns.heatmap(titanic.corr(), cmap='coolwarm')


# ### Soal 7
# 
# Buatlah FacetGrid & di dalamnya terdapat histogram dari data di atas yang hasilnya seperti di bawah ini

# In[12]:


fg = sns.FacetGrid(titanic, col='sex')
fg = fg.map(plt.hist, 'age')


# In[ ]:





# In[ ]:




