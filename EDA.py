# python-learning
import pandas as pd
import matplotlib.pyplot as plt
#df=pd.read_csv('~hesam\Downloads\data bases-python learning\ netflix-data.csv')
data_path="C:/Users/hesam/Downloads/data bases-python learning/netflix-data.csv"
df=pd.read_csv(data_path)
#print(df2.head())
print(df.columns)
fig,(ax1,ax2)=plt.subplots(1,2)
#unique_value=df2['User ID'].nunique()
#new_df=df.groupby(['Subscription Type']).sum().sort_values('Monthly Revenue',ascending=False)
revenue_sum=df.groupby(['Subscription Type'])['Monthly Revenue'].sum().sort_values()
revenue_count=df.groupby('Subscription Type')['Monthly Revenue'].count().sort_values()

revenue_sum.plot(kind='barh',ax=ax1,color='blue', figsize=(10,2))
revenue_count.plot(kind='bar',ax=ax2 ,color='green',figsize=(10,2))

ax1.set_xlabel('sum of revenue')
ax1.set_ylabel('subscription type')
ax2.set_xlabel('subscription type')
ax2.set_ylabel('count of revenue')

for i,value in enumerate(revenue_sum):
    ax1.annotate(f'{value:.0f}',(value-1000,i),ha='center', va='bottom')


for i,value in enumerate(revenue_count):
    ax2.annotate(str(value),(i,value),ha='center', va='bottom')


def age_classifier(age):
    if age< 15: return 'under 15'
    elif age>=16 and age<=35: return 'between 16 and 35'
    elif age>35 and age<50: return 'between 35 and 50'
    else: return 'above 50'
df['age group']=df['Age'].apply(age_classifier)
age_group_counts = df.groupby(['age group', 'Subscription Type']).size().unstack(fill_value=0)
#table=pd.pivot_table(df,values='Subscription Type',index='age group',aggfunc='count',fill_value=0)
fig, ax = plt.subplots()

table_chart = ax.table(cellText=age_group_counts.values, colLabels=age_group_counts.columns, rowLabels=age_group_counts.index, loc='center', cellLoc='center')

#new_df=df.groupby('age group')['Subscription Type'].count().sort_values().plot(kind='bar',color='green', figsize=(10,2))
#new_df
ax.axis('off')
df['Join Date']=pd.to_datetime(df['Join Date'])
df['Last Payment Date']=pd.to_datetime(df['Last Payment Date'])
fig, ax=plt.subplots()
Join_counts=df.groupby(['Join Date'])['User ID'].count().sort_values().plot(kind='line',ax=ax,figsize=(12,6))
plt.show()
df['Loyalty_Duation']=(df['Last Payment Date']-df['Join Date'])
df.sort_values('Loyalty_Duation',ascending=True)
#df2['User ID'].value_counts().plot(kind='bar')
# for column in df2.columns:
#     plt.figure()
#     plt.plot(df2[column])
#     plt.title(column)
#     plt.show()

