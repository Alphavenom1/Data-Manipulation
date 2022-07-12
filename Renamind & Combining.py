#setup
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")

#egion_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed=reviews.rename(columns={'region_1':'region','region_2':'locale'})

#Set the index name in the dataset to wines.
reindexed=reviews.rename_axis('wines',axis='rows')

#Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products,movie_products])

#Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. Using this, generate a dataset combining the two tables into one.
left=powerlifting_meets.set_index('MeetID')
right=powerlifting_competitors.set_index('MeetID')
powerlifting_combined = left.join(right,lsuffix='_meets',rsuffix='_comp')
