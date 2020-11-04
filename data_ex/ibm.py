
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import stats

#What is the correct mean and standard deviation of the quantity of pasta purchased by time unit by household?

c=pd.read_csv('ibm_course.csv')
#print(c.columns)
df=DataFrame(c.head(100))
#print(df.head(100))

#check data types

x=df.dtypes
#print(x)

#change data types to category
age=df.Age=pd.Categorical(df['Age'], ordered=True)

#group transaction by age 
x=df.groupby('Age').mean()
print(x)






















































