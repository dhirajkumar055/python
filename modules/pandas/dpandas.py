#May30,2020
#Bahadurgarh
import pandas as pd
#DheerajKumarChopra
df=pd.read_csv('../../files/csv/file.csv')
print("Maximum age:",df['age'].max())
print()
print("All Males:")
print(df['name'][df['gender']=='M'])
print()
print("All Females:")
print(df['name'][df['gender']=='F'])
print()
print("Average Age :",df['age'].mean())
print()
print(df.transpose())
