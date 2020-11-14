import numpy as np
import pandas as pd
import toml
from pandas_preprocessor import *
import os


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def build():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    tomlLoc = os.path.join(this_dir, "config.toml")
    print(tomlLoc)
    config = toml.load(tomlLoc)
    fileLoc = os.path.join(this_dir, config['data']['connectionstring'])
    print(fileLoc)
    config['data']['connectionstring'] = fileLoc

    df = get_dataframe(config['data'])

    # foreach(print, l(df))
    cleaned_df = clean_dataframe(df, config['dataframe'])
    # cleaned_df['Grass'] = pd.to_numeric(cleaned_df['Grass'], downcast=None)
    # cleaned_df['Grass'] = cleaned_df['Grass'].astype('object')
    # foreach(print, l(cleaned_df))
    foreach(print, l(invert_cleaning(cleaned_df, config['dataframe'])))


build()
