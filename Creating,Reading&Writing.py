# Setup
import pandas as pd

#Create a DataFrame fruits
fruits = pd.DataFrame({'Apples':[30] ,'Bananas':[21]})

#Create a dataframe fruit_sales that matches the diagram



fruit_sales =pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])

#Create a variable ingredients with a Series
ingredients =pd.Series(['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'],name='Dinner')

#read the following csv dataset of wine reviews into a DataFrame called reviews
reviews =pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv",index_col=0)

#cows_and_goats.csv
animals.to_csv("cows_and_goats.csv")
