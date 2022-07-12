#setup
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

#What is the data type of the points column in the dataset?
dtype = reviews.points.dtype
print(dtype) #int64

#Create a Series from entries in the points column, but convert the entries to strings. 
point_strings = reviews['points'].astype('str')

#Sometimes the price column is null. How many reviews in the dataset are missing a price?
n_missing_prices =pd.isnull(reviews.price).sum()
print(n_missing_prices) #8996

#What are the most common wine-producing regions?
 reviews.region_1.fillna("Unknown")
 reviews_per_region =reviews.groupby('region_1').size().sort_values(ascending=False)
 reviews_per_region                                                     

#or

 reviews_per_region =reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
 reviews_per_region
