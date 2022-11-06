#!/usr/bin/env python
# coding: utf-8

# # EDA ON ZOMATO DATASET

# # IMPORTING LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # IMPORTING DATASET

# In[10]:


df=pd.read_csv("E:\\DATA SCIENCE\\Project\\python\\zomato\\zomato.csv",encoding='latin-1')


# # READING THE 1ST 10 ROWS

# In[11]:


df.head()


# # UNDERSTANDING THE DATASET

# In[12]:


df.info()


# # GETTING THE ROWS & COLUMN

# In[14]:


df.shape


# # GETTING NUMERICAL VALUES AND VARIABLES

# In[17]:


df.describe()


# # GETTING THE SUM OF NULL / MISSING VALUES

# In[18]:


df.isnull().sum()


# SO THERE ARE 9 MISSING VALUES

# # FINDING OUT THE VALUE WHERE NULL VALUES > 0 BY USING LIST COMPREHENSIONS

# In[22]:


[i for i in df.columns if df[i].isnull().sum()>0]


# WE FOUND 'CUISINES' COLUMN HAVING NULL VALUE

# In[28]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# WE DO NOT HAVE MANY NULL VALUES. SO, WE ARE NOT ABLE TO SEE ANY. 

# # IMPORTING ANOTHER DATASET i.e. COUNTRY CODE

# In[30]:


df_Country=pd.read_excel('E:\\DATA SCIENCE\\Project\\python\\zomato\\Country-Code.xlsx')


# # GETTING THE TOP ROWS

# In[31]:


df_Country.head()


# # COMBINING THE TWO DATAFRAME & DISPLAYING TOP 5 ROWS

# In[33]:


df_final=pd.merge(df,df_Country,on='Country Code',how='left')
df_final.head(5)
#on: The common table
#how: type of join


# # To check Datatypes

# In[35]:


df_final.dtypes


# # HOWMANY DIFFERENT COUNTRIES ARE THERE AND DISPLAY THEIR RESPECTIVE RECORDS

# In[56]:


df_final.Country.value_counts()


# # DISPLAYING ONLY THE COUNTRY NAME

# In[68]:


country_names=df_final.Country.value_counts().index


# # VALUES OF EACH COUNTRY

# In[72]:


country_value=df_final.Country.value_counts().values


# # WHICH COUNTRY PROVIDING MAXIMUM ORDERS [PIE CHART]

# In[73]:


plt.pie(country_value,labels=country_names)


# In[ ]:


#INDIA IS GIVING MAXIMUM ORDERS


# # TOP3 COUNTRIES PROVIDING MAXIMUM ORDERS

# In[74]:


plt.pie(country_value[:3],labels=country_names[:3])


# In[ ]:


#TOP3 : INDIA > USA > UK


# # PERCENTAGE OF ORDER THAT EACH COUNTRY CONTRIBUTES

# In[82]:


plt.pie(country_value[:3],labels=country_names[:3],autopct='%1.1f%%')


# In[ ]:


#Observation:
#Zomato's Maximum Transaction Records are from India,
#After India USA then UK comes.


# # reading the columns that are available

# In[83]:


df_final.columns


# # Let us know the Rating, color and respective categories.

# In[85]:


df_final.groupby(['Aggregate rating', 'Rating color','Rating text']).size()


# In[88]:


df_final.groupby(['Aggregate rating', 'Rating color','Rating text']).size().reset_index()


# # NOW LET'S REPLACE THIS 0 INDEX WITH 'RATING COUNT'

# In[92]:


ratings=df_final.groupby(['Aggregate rating', 'Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating_Count'})
ratings.head(10)


# #OBSERVATION
# 1. RATING BETWEEN 4.5 TO 4.9 => EXCELLENT
# 2. RATING BETWEEN 4.0 TO 3.4 => VERY GOOD
# 3. RATING BETWEEN 3.5 TO 3.9 => GOOD
# 4. RATING BETWEEN 3.0 TO 3.4 => AVERAGE
# 5. RATING BETWEEN 2.5 TO 2.9 => AVERAGE
# 6. RATING BETWEEN 2.0 TO 2.4 => POOR
# 7. 2148 CUSTOMER HAS NOT GIVEN ANY RATING.

# In[94]:


sns.barplot(x='Aggregate rating',y='Rating_Count',data=ratings)


# # Let's make this dig Bigger.

# In[96]:


plt.rcParams['figure.figsize']=(12,6)
#rcparams:used to change any parameters if we want.
sns.barplot(x='Aggregate rating',y='Rating_Count',data=ratings)


# # Let's assign the color to tha ratings as per our dataset. 

# In[102]:


plt.rcParams['figure.figsize']=(12,6)
#rcparams:used to change any parameters if we want.
sns.barplot(x='Aggregate rating',y='Rating_Count',hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])
#hue : to get the label of colors. 


# # OBSERVATION:
# 1. Count of 'NOT RATED' is very high.
# 2. Maximum number of rating is between 3.0 to 3.4

# In[105]:


#count plot
sns.countplot(x='Rating color',data=ratings, palette=['blue','red','orange','yellow','green','green'])


# In[108]:


ratings.head(10)


# # FIND THE COUNTRIES THAT HAS GIVEN 0 RATINGS

# In[117]:


df_final.columns


# In[128]:


df_final.columns


# In[130]:


df_final.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# OBSERVATION:
# INDIAN CUSTOMERS HAS GIVEN ZERO RATING.

# # WHICH CURRENCY IS USED BY WHICH COUNTRY

# In[137]:


df_final[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# # which country do have online delivery

# In[138]:


df_final[df_final['Has Online delivery']=='Yes'].Country.value_counts()


# OBSERVATION:
#     1. Online delivery is available in UAE& INDIA.

# # CREATING PIE CHART FOR TOP 5 CITIES DISTRIBUTION

# In[139]:


df_final.City.value_counts().index


# In[147]:


city_values=df_final.City.value_counts().values
city_labels=df_final.City.value_counts().index


# In[150]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# # TOP10 CUISINES 

# In[157]:


df_final.head(2)


# In[194]:


df_final.groupby(['Cuisines']).size().reset_index().head(10)


# In[203]:


df_TOP10=df_final.groupby(['Cuisines']).size().reset_index().rename(columns={0:'TOP10'})
df_TOP10.head(10)


# In[208]:


df_TOP10.sort_values(by=['TOP10'],ascending=False).head(10)

