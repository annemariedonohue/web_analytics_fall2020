#!/usr/bin/env python
# coding: utf-8

# code for cleaning ratings; seperating dates into just year; finding mean and mode

# In[92]:


#import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[93]:


#opening nolita info in csv 
nolita=pd.read_csv("Tacombi Nolita Yelp Crawl-Cleaned Data.csv")
#showing top 5 rows
nolita.head()


# In[155]:


#new dataframe of nolita's field rating
rating=nolita['rating']
#getting the first character of the string into a different column named ratingNum
nolita['ratingNum']=nolita['rating'].str[0]
#quantifing ratingNum for analytics- changing from string to integer 
nolita['ratingNum']= nolita['ratingNum'].astype(int)

#new dataframe 
date=nolita['date']
#getting year of the date- putting into new column dateYear
nolita['dateYear'] = pd.DatetimeIndex(nolita['date']).year

#exporting to new csv
csv=nolita.to_csv('nolita.csv')
#print Nolita mean 
print(nolita.ratingNum.mean())
#print Nolita median 
print(nolita.ratingNum.median())


# In[156]:


#read bleekers csv
bleeker=pd.read_csv("Tacombi Bleecker Yelp Crawl-Cleaned Data.csv")
#new dataframe of bleeker's field rating
rating=bleeker['rating']
#getting the first character of the string into a different column named ratingNum
bleeker['ratingNum']=bleeker['rating'].str[0]
#quantifing ratingNum for analytics- changing from string to integer 
bleeker['ratingNum']= bleeker['ratingNum'].astype(int)

#new dataframe
date=bleeker['date']
#getting year of the date- putting into new column dateYear
bleeker['dateYear'] = pd.DatetimeIndex(bleeker['date']).year

#exporting to new csv
csv=bleeker.to_csv('bleeker.csv')
#print bleeker mean
print(bleeker.ratingNum.mean())
#print bleeker median
print(bleeker.ratingNum.median())


# In[ ]:




