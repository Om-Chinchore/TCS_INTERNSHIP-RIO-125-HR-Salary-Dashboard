#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# In[2]:


# Load the dataset (replace 'data.csv' with your dataset file)
data = pd.read_csv("C:/Users/Om Chinchore/Desktop/TCS/HR_Data.csv")


# In[5]:


# Encode categorical variables (if any)
encoder = LabelEncoder()
data['Position'] = encoder.fit_transform(data['Position'])
data['Department'] = encoder.fit_transform(data['Department'])
data['State'] = encoder.fit_transform(data['State'])
print(data.head())


# In[7]:


# Split the data into features (X) and target (y)
X = data[['Position', 'Department','State']]
y = data['Salary']


# In[8]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[9]:


# Create a Linear Regression model
model = LinearRegression()


# In[10]:


# Fit the model to the training data
model.fit(X_train, y_train)


# In[11]:


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:",mae)
print("Mean Squared Error:",mse)
print("R-squared:",r2)


# In[13]:


# Example: Predict salary for a new HR professional
new_data = pd.DataFrame({'Position': [19], 'Department': [22], 'State': [4]})
predicted_salary = model.predict(new_data)
print("Predicted Salary:",predicted_salary[0])


# In[ ]:





# In[ ]:




