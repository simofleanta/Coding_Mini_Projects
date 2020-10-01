import pandas as pd
import seaborn as sns 


vote=pd.read_csv('presence.csv')
print(vote.columns)


v = sns.boxplot(data=vote, x="LP", y="LT")
is1 = sns.distplot(vote["LT"])






