
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
df=DataFrame(c.head(13))
#print(df.head(100))

#check data types

x=df.dtypes
#print(x)

#change data types to category
age=df.Age=pd.Categorical(df['Age'], ordered=True)
userid=df.User_id=pd.Categorical(df['User_id'], ordered=True)
ip=df.IP_Address=pd.Categorical(df['IP_Address'])


#group transaction by age 
d=df.groupby(['IP_Address']).sum()
print(d)

f=['mean', 'std']
x=df.groupby(['data'], as_index=False)[['Transaction_value']].agg(f)


#copy dataset with desired columns
s=df[['Transaction_value','Age','Unit_Purchased','data']].copy()

#make corr
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap='Blues')























































