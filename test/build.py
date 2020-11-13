import numpy as np
import pandas as pd
import toml
from clean import *
from encoders.index import encoder_selector


config = toml.load("test/config.toml")

df = get_dataframe(config['data'])

# l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

# foreach(print, l)
print(df.head())
cleaned_df = clean_dataframe(df, config['dataframe'])
print(cleaned_df.head())
print(invert_cleaning(cleaned_df, config['dataframe']).head())
