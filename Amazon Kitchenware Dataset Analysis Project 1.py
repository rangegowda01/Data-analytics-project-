#!/usr/bin/env python
# coding: utf-8

# ## Project Title : Amazon Kitchenware Dataset Analysis Project 1
# 
# ## Purpose
#  
# Analyzing the Amazon Kitchenware Dataset with Python libraries like pandas and matplotlib enables businesses to extract valuable insights for informed decision-making. It helps in understanding customer preferences, identifying market trends, analyzing seasonal patterns, assessing customer sentiment, understanding pricing dynamics, facilitating inventory management, developing recommendation systems, and conducting competitor analysis. Overall, leveraging this dataset empowers businesses in the kitchenware industry to optimize their product offerings, marketing strategies, and operational efficiency to meet customer needs and maximize performance.

# ## Step 1 : Installing the Packages beforehand

# In[37]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[114]:


# Importing the necessary packages for data manipulation and visualisation

import pandas as pd  # data manipulation
import matplotlib.pyplot as plt # data visualization


# ## Step 2 : Loading the files from the local system to the Notebook

# In[34]:


# Load the files

data = pd.read_csv('C:/Project/amazon_kitchenware.csv')  # To read the csv file from the file path 
print(data)


# ## Step 3 : Data view

# In[13]:


# print the first 5 rows of the dataset
data.head() 


# In[14]:


# To print the column names present in the dataset
data.columns


# In[15]:


# Display the summary information about Dataframe
data.info


# In[16]:


# Print the shape of the dataset
data.shape


# In[17]:


# To display the data types of each column in a DataFrame
data.dtypes


# In[18]:


# Display the summary statistics for numerical columns in a DataFrame
data.describe


# ## Step 4 : Data cleaning / Filteration / Manipulation

# In[19]:


# Display the number of rows in a particular column
data.count()


# In[20]:


# To get the count of unique values in each column of a DataFrame
data.value_counts


# In[21]:


# It containing all unique values in the 'brand' column of the DataFrame
data['brand'].unique()


# In[22]:


#  drops rows with missing values
data.dropna()


# In[23]:


# Print the shape of the dataset
data.shape


# In[24]:


# check the rows if any cell is null value then replace with True
data.dropna(inplace=True)


# In[48]:


#  used to identify duplicated values in specified column
data['description'].duplicated()


# In[26]:


# used to identify duplicated values and replace by True
data.drop_duplicates(inplace=True)


# In[27]:


# Display the number of duplicate rows found in the DataFrame.
duplicate_rows = data.duplicated() 
print(duplicate_rows.sum())


# ##  Step 5 : Data Sorting / Searching / Validation

# In[28]:


# Display the reviwes count in shuffeled order
data['reviewsCount']


# In[29]:


# arranging the values of reviewsCount in ascending order
data.sort_values('reviewsCount',ascending=True)


# In[30]:


# arranging the values of reviewsCount in descending order
data.sort_values('reviewsCount',ascending=False)


# In[44]:


# to filter the price/value data which is greater than 50
df = data[data['price/value'] > 50]['price/value']
print(df)


# ## Step 6 : Data Visualization

# In[122]:


# to creates a DataFrame containing the first 20 rows of the original data.
df = pd.DataFrame(data.head(10))

# calculates the frequency of each unique value in the 'stars' column of the DataFrame and display the percentage of each slice.
df['asin'].value_counts().plot(kind='pie',autopct='%1.1f%%')

# to give the title of the plot
plt.title('Frequency of ASINs')

# to display the pie chart
plt.show()   


# In[94]:


# to creates a DataFrame containing the first 20 rows of the original data.
df = pd.DataFrame(data.head(15))

# calculates the frequency of each unique value in the 'stars' column of the DataFrame and display the percentage of each slice.
df['brand'].value_counts().plot(kind='bar', color='Blue')

# Set the label for the x-axis
plt.xlabel('brand')

# Set the label for the y-axis
plt.ylabel('price/value')

# to give the title of the plot
plt.title('Frequency of Brands')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=60)

# to display the pie chart
plt.show()  


# In[101]:


# to creates a DataFrame containing the first 20 rows of the original data.
df = pd.DataFrame(data.head(15))

# calculates the frequency of each unique value in the 'stars' column of the DataFrame and display the percentage of each slice.
df['stars'].value_counts().plot(kind='line', color='Brown')

# Set the label for the x-axis
plt.xlabel('stars')

# Set the label for the y-axis
plt.ylabel('price/value')

# to give the title of the plot
plt.title('Frequency of Stars')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0)

# to display the pie chart
plt.show()  


# In[108]:


# to creates a DataFrame containing the first 20 rows of the original data.
df = pd.DataFrame(data.head(15))

# calculates the frequency of each unique value in the 'stars' column of the DataFrame and display the percentage of each slice.
df['stars'].value_counts().plot(kind='hist', color='Yellow')

# Set the label for the x-axis
plt.xlabel('stars')

# Set the label for the y-axis
plt.ylabel('price/value')

# to give the title of the plot
plt.title('Frequency of Stars')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0)

# to display the pie chart
plt.show()  


# In[113]:


# to creates a DataFrame containing the first 20 rows of the original data.
df = pd.DataFrame(data.head(15))

# calculates the frequency of each unique value in the 'stars' column of the DataFrame and display the percentage of each slice.
df['stars'].value_counts().plot(kind='barh', color='Red')

# Set the label for the x-axis
plt.xlabel('stars')

# Set the label for the y-axis
plt.ylabel('price/value')

# to give the title of the plot
plt.title('Frequency of Stars')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0)

# to display the pie chart
plt.show()  


# In[130]:


# Create a DataFrame containing the first 15 rows of the original data
df = pd.DataFrame(data.head(15))

# Calculate the frequency of each unique value in the 'stars' column
stars_freq = df['stars'].value_counts()

# Create x and y values for the scatter plot
x_values = stars_freq.index
y_values = stars_freq.values

# Plot the scatter plot
plt.scatter(x_values, y_values, color='Black')

# Set the label for the x-axis
plt.xlabel('Stars')

# Set the label for the y-axis
plt.ylabel('price/value')

# Set the title of the plot
plt.title('Frequency of Stars')

# Display the plot
plt.show()


# In[ ]:




