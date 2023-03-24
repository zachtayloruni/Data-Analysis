#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Part 1


# In[31]:


#Example


# In[8]:


#My Attempt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

job = pd.read_csv('job-market(3).csv')
job.head()


# In[9]:


#My Attempt
#Plot based on number of jobs by job classification

plt.figure(figsize=(10,10))
classification = sns.countplot(y='Classification', data=job, order=job['Classification'].value_counts().index)
classification.set(xlabel ='Number of jobs', ylabel = 'Classification', title ='Jobs and Number of Postings')


# In[ ]:





# In[11]:


#Part 2


# In[9]:


#Example
#create dataframe for salary ranges


# In[43]:


#Example
#salary ranges plot


# In[6]:


#My Attempt

lowestDf = job[job['LowestSalary'].isna()==False]
lowestDf = lowestDf.groupby('LowestSalary').count()
lowestDf['LowestSalary'] = lowestDf.index
lowestDf['Count'] = lowestDf["Id"]
lowestDf.head()


# In[17]:


#My Attempt

fig, ax = plt.subplots()

colours = sns.color_palette('pastel')[0:4]

ax.pie(lowestDf['Count'], labels=lowestDf['LowestSalary'], colors=colours, autopct='%.0f%%')
ax.add_patch(plt.Circle((0, 0), 0.4, color='white'))
ax.set_title('Job Postings by Salary Range')
ax.autoscale()


# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


#OPTIONAL

locationDf = job[job['Location'].isna()==False]
locationDf = locationDf.groupby('Location').count()
locationDf['Location'] = locationDf.index
locationDf = locationDf[['Id', 'Location']]
locationDf


# In[35]:


fig, ax = plt.subplots()

ax.pie(x=locationDf['Id'], labels=locationDf['Location'], autopct='%.0f%%')


# In[ ]:





# In[14]:


#OPTIONAL

get_ipython().run_line_magic('matplotlib', 'inline')
# Pie char for job market share of cities
from matplotlib import cm


# In[ ]:




