#setup
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

#Who are the most common wine reviewers in the dataset
reviews_written=reviews.groupby('price')['points'].max().sort_index()

#What are the minimum and maximum prices for each variety of wine?
price_extremes=reviews.groupby('variety')['prices'].agg([min,max])

#What are the most expensive wine varieties? Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price
sorted_varieties = price_extremes.sort_values(by=['min','max'],ascending=False)
sorted_varieties

#Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the taster_name and points columns.
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

#What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
