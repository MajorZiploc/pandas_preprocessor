import numpy as np
import pandas as pd
import toml
from pandas_preprocessor import *
import os


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, l(df))


def build():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    tomlLoc = os.path.join(this_dir, "config.toml")

    config = toml.load(tomlLoc)

    set_full_paths(config, this_dir)

    df = get_dataframe(config['data'])

    # df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

    print('OG DF')
    p(df)

    cleaned_df = clean_dataframe(df, config['dataframe'])
    print('Cleaned DF')
    p(cleaned_df)

    inverted_df = invert_cleaning(cleaned_df, config['dataframe'])
    print('Inverted DF')
    p(inverted_df)


build()
