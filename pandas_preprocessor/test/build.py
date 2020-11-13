import numpy as np
import pandas as pd
import toml
from pandas_preprocessor import *
import os

this_dir = os.path.dirname(os.path.realpath(__file__))
tomlLoc = os.path.join(this_dir, "config.toml")
print(tomlLoc)
config = toml.load(tomlLoc)
fileLoc = os.path.join(this_dir, config['data']['connectionstring'])
print(fileLoc)
config['data']['connectionstring'] = fileLoc

df = get_dataframe(config['data'])

# l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

# foreach(print, l)
print(df.head())
cleaned_df = clean_dataframe(df, config['dataframe'])
print(cleaned_df.head())
print(invert_cleaning(cleaned_df, config['dataframe']).head())
