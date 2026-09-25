# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:51:20 2025

@author: ellen
"""

import pandas as pd

#write from csv to dataframe
#make sure spyder is operating in the correct directory
df=pd.read_csv("Renewable_Energy_Adoption.csv")

#display first 5 rows
df.head()

#short description, lists all columns with entry data types
df.info()

#gives a statistical summary of dataframe
df.describe()

#summary statistics about certain column
df.describe()["Total Energy Consumption (TWh)"]

#access info from first row
#gives data for year 2000
df.loc[0]

#find those countries with renewable energy
#usage greater than 76%
df[df["Renewable Energy (%)"]>75]
#look at just the first row of these
df[df["Renewable Energy (%)"]>75].iloc[0] #iloc finds on index, loc finds on label

#sort based on highest renewable energy
df_renewable_sort=df.sort_values("Renewable Energy (%)", ascending=False)
#use iloc here as loc still connected to old labels
df_renewable_sort.iloc[0] #look at top country

"cleaning data"
#delete rows with missing values
df.dropna() #deletes alot

#fill missing values with 0 
#need to assign to dataframe
#df=df.fillna(0)



#create new column 
#solar as percentage of total
renewables=['Solar', 'Wind', 'Hydro', "Geothermal", "Biomass", "Other Renewables"]
#axis=1 means to apply the sum row-wise
#df["Renewables total"]=df[renewables].sum(axis=1)
#df["solar (%) renewables"]=df["Solar"]/df["Renewables total"]

df["Renewable Energy calculated(%)"]=df[renewables].sum(axis=1)





