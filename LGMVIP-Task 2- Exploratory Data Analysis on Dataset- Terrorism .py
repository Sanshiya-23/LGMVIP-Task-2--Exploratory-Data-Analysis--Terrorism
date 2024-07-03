#!/usr/bin/env python
# coding: utf-8

# # LGMVIP-Task 2- Exploratory Data Analysis- Terrorism 

# # Step 1: Analyse the dataset
# 
# The first few rows of the dataset are displayed to get an overview, and the code then identifies and prints the columns with missing values. To ensure data integrity, rows with missing values in the 'approxdate' column are removed. Descriptive statistics and information about the dataset are then generated to understand its structure and content. The code visualizes the number of terrorist attacks over the years using a count plot, which highlights trends and patterns in the frequency of attacks. The plot is customized with titles, axis labels, and rotated x-axis labels for better readability. This initial analysis provides a foundation for more in-depth exploration and insights into global terrorism data.

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


# Load the dataset
df = pd.read_csv(r'C:\Users\SANSHIYA\Downloads\Global Terrorism - START data (1)\globalterrorismdb_0718dist.csv',encoding='ISO-8859-1')

# Display the first few rows of the dataset
df.head()


# In[29]:


missing_values=df.isnull().sum()
print(missing_values[missing_values>0])


# In[30]:


df=df.dropna(subset=['approxdate'])


# In[31]:


df.describe()


# In[32]:


df.info()


# # Step 2: Data Visualization
# 
# The provided code generates several visualizations to analyze and understand patterns in a global terrorism dataset. Each plot is designed to highlight different aspects of the data, providing valuable insights into the trends and distributions of terrorist incidents.
# 

# In[33]:


plt.figure(figsize=(12,6))
sns.countplot(x='iyear',data=df)
plt.title('Number of terrorist attack over the years')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=90)
plt.show()


# This plot shows the frequency of terrorist attacks for each year in the dataset. Peaks and troughs in the plot indicate periods with higher and lower terrorist activities.This visualization helps identify temporal trends and patterns in terrorist activity, revealing how the frequency of attacks has changed over time.

# In[34]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='longitude',y='latitude',hue='region_txt',data=df,palette='viridis')
plt.title('Geographical Distribution of Terrorist Incidents')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# This scatter plot displays the geographic locations of terrorist incidents, color-coded by region. It shows the spatial distribution and regional hotspots of terrorist activity.This visualization provides a geographical perspective on terrorism, helping to identify regions that are more affected and allowing for spatial analysis of incident patterns.

# In[35]:


plt.figure(figsize=(12,8))
sns.countplot(y='attacktype1_txt', data=df, order=df['attacktype1_txt'].value_counts().index)
plt.title('Distribution of Attack type')
plt.xlabel('Count')
plt.ylabel('Attack Type')
plt.show()


# This horizontal bar plot shows the distribution of different types of terrorist attacks, ordered by their frequency. It highlights which types of attacks are most and least common.This visualization helps in understanding the diversity and prevalence of various attack methods used in terrorist activities, providing insight into common tactics.

# In[36]:


plt.figure(figsize=(10,6))
sns.countplot(y='targtype1_txt', data=df, order=df['targtype1_txt'].value_counts().index)
plt.title('Distribution of Target Types')
plt.xlabel('Count')
plt.ylabel('Target Type')
plt.show()


# This horizontal bar plot shows the distribution of different types of targets of terrorist attacks, ordered by their frequency. It indicates which types of targets are most frequently attacked.This visualization provides insight into the types of entities (e.g., civilians, government, businesses) that are most frequently targeted in terrorist incidents, which is crucial for understanding the impact and focus of terrorist activities.

# # Step 3: Analyzing the Impact and Correlations of Terrorist Attacks
# 
# In this stage, we investigate the distributions of the number of fatalities and injuries in order to get deeper into the analysis of the effects of terrorist acts. In order to comprehend the relationships between many important factors, we also investigate the correlations between them.

# In[37]:


plt.figure(figsize=(10,6))
sns.histplot(df['nkill'], bins=50, kde=True)
plt.title('Distribution of Number of Killed in Attacks')
plt.xlabel('Number Killed')
plt.ylabel('Frequency')
plt.show()


# This histogram, accompanied by a kernel density estimate (KDE), shows the frequency distribution of the number of people killed in terrorist attacks. It provides insight into how common various levels of fatalities are.Understanding the distribution of fatalities helps gauge the severity of terrorist attacks and identify common fatality ranges.

# In[38]:


plt.figure(figsize=(10,6))
sns.histplot(df['nwound'], bins=50, kde=True)
plt.title('Distribution of Number of Wounded in Attacks')
plt.xlabel('Number Wounded')
plt.ylabel('Frequency')
plt.show()


# This histogram, also with a KDE, displays the frequency distribution of the number of people wounded in terrorist attacks. It highlights how often different levels of injuries occur.Analyzing the distribution of injuries provides insight into the broader impact of terrorist attacks on populations, complementing the fatality analysis.

# In[39]:


# Select relevant columns
columns_of_interest = ['nkill', 'nwound','iyear', 'country','latitude', 'longitude']
df_selected = df[columns_of_interest]

# Calculate the correlation matrix
correlation_matrix = df_selected.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Selected Variables')
plt.show()


# This heatmap displays the correlation matrix of selected variables, including the number of people killed and wounded, the year of the attack, the country, and the geographical coordinates (latitude and longitude). The annotations indicate the strength and direction of the correlations.The correlation analysis helps identify relationships between different variables, such as whether more recent years see higher fatalities or if certain regions are more prone to severe attacks. Understanding these correlations can inform strategies for preventing and mitigating the impacts of terrorism.
