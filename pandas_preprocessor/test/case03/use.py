from pandas_preprocessor import *
import os
import toml


# import Pandas as pd
import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John__Larter', 'Robert__Junior_dsf', 'Jonny__Depp'],
                   'Age': [32, 34, 36]})

print("Given Dataframe is :\n", df)

print("\nSplitting Name column into two different columns :")

# splitting 'Name' column into Two columns
# i.e. 'First' and 'Last'respectively and
# Adding these columns to the existing dataframe.
df[['First', 'Last']] = df['Name'].apply(
    lambda x: pd.Series(str(x).split("__", 1)))

print(df)


this_dir = os.path.dirname(os.path.realpath(__file__))
config_name = "config.toml"

# Loads config
tomlLoc = os.path.join(this_dir, config_name)
config = toml.load(tomlLoc)

# prefix all file locations with this directory
set_full_paths(config, this_dir)
# Loads pickled model
# model = load_model(config)

# get user query
df = get_dataframe(config['data'])

# clean user query for models consumption
# house_data = df.drop(['Address', 'Method', 'SellerG', 'Date',
#                       'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)
cdf = clean_dataframe(df, config['dataframe'])
# outputColumnNames = [o['name'] for o in config['dataframe']['outputs']]
# house_to_value = house_data.drop(outputColumnNames, axis=1)

print('Cleaned DF')
print(cdf.head())

# # ask the model the user query
# predicted_house_value = model.predict(house_to_value)

# predicted_house_value = predicted_house_value[0]

# # Print estimated value of the property to two decimal places
# print("This property has an estimated value of AUD %.2f" %
#       predicted_house_value)

# # Transform user query back to users data structure
idf = invert_cleaning_query(cdf, config['dataframe'])

print('Inverted DF')
print(idf.head())
