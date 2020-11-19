import pandas as pd
import toml
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import math
import joblib
from pandas_preprocessor import *
import os


def ldf(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, ldf(df))


this_dir = os.path.dirname(os.path.realpath(__file__))
config_name = "config.toml"

# Loads config
tomlLoc = os.path.join(this_dir, config_name)
config = toml.load(tomlLoc)

# prefix all file locations with this directory
set_full_paths(config, this_dir)

# get training/test data
df = get_dataframe(config['data'])

r = clean_dataframe(df, config['dataframe'])

print('Cleaned DF')
p(r)
outputColumnName = [o['name'] for o in config['dataframe']['outputs']][0]
X = r.drop(outputColumnName, axis=1)
y = r[outputColumnName]

inverted_df = invert_cleaning(r, config['dataframe'])
print('Inverted DF')
p(inverted_df)
