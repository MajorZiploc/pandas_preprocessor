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
    print(tomlLoc)
    config = toml.load(tomlLoc)
    fileLoc = os.path.join(this_dir, config['data']['connectionstring'])
    print(fileLoc)
    config['data']['connectionstring'] = fileLoc

    inputs = config['dataframe']['inputs']

    for i in inputs:
        es = i.get('encoding_steps', [])
        for e in es:
            fl = nc(lambda: e['settings']['file_location'])
            if (fl is not None):
                e['settings']['file_location'] = path.join(this_dir, fl)

    df = get_dataframe(config['data'])

    print('OG DF')
    p(df)

    cleaned_df = clean_dataframe(df, config['dataframe'])
    print('Cleaned DF')
    p(cleaned_df)

    inverted_df = invert_cleaning(cleaned_df, config['dataframe'])
    print('Inverted DF')
    p(inverted_df)


build()
