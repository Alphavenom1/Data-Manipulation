#Setup
import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

#What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()
#What countries are represented in the dataset? (Your answer should not include any duplicates.)
countries = reviews.country.unique()
#How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
reviews_per_country = reviews.country.value_counts()
#Create variable centered_price containing a version of the price column with the mean price subtracted.
centered_price = reviews.price-reviews.price.mean()
#Which wine is the "best bargain"? Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
maxratio_index=(reviews.points/reviews.price).idxmax()
bargain_wine=reviews.loc[maxratio_index,'title']
#Create a Series descriptor_counts counting how many times each of these two words appears in the description column in the dataset. 
fruit_count=reviews.description.map(lambda description:"fruity"in description).sum()
tropical_count=reviews.description.map(lambda description:"tropical"in description).sum()
descriptor_counts=pd.Series([tropical_count,fruit_count],index=["tropical wines ","fruity wines"])
descriptor_counts

#reate a series star_ratings with the number of stars corresponding to each review in the dataset.
def stars(row):
    if row.points>=95:
        return 3
    elif row.country=="Canada":
        return 3
    elif row.points>=85:
        return 2
    else:return 1
star_ratings=reviews.apply(stars,axis="columns")
star_ratings

