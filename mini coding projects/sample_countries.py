import pandas as pd
import pandas as DataFrame
import seaborn as sns 
import matplotlib.pyplot as plt

"""Analyze and visualize population in coauntries. Data is a fake sample data from google
data on a certain country and population slicing
data on a certain country and population slicing
extract population column and do the mean of it. 
print population on a certain country+slice it and perform mean
charts"""

country=pd.read_csv('countries.csv')
print(country.head(10))
print(country.columns)

#
Romania=country[country.country=='Romania']
print(Romania)
Ro=Romania.population.iloc[0:12]
print(Ro)
Roy=Romania.year.iloc[0:12]
print(Roy)
country.columns=['country','year','population']

#
p=country.population
p_mean=p.mean
print(p_mean)

country['Mean_population']=p.mean
print(country.columns)

#
Romania=country[country.country=='Romania']
R0=Romania.population.iloc[:5]
print(Ro.head(3))
r=Romania.population
r_mean=r.mean
print(r_mean)
#------------------------------------------------------------------------

"""Perform charts on the data"""
print(country.head(0))
print(country.columns)
p=country.population
p_mean=p.mean
print(p_mean)

vis1 = sns.distplot(country["population"])
vis2= sns.lmplot(data=country, x='year', y='population',
                 fit_reg=False)

vis1 = sns.distplot(country["population"])
vis3= sns.lmplot(data=country, x='country', y='population',
                 fit_reg=False)

vis4= sns.boxplot(data=country, x="year", y="population")

sns.pairplot(country)
plt.show()




































































