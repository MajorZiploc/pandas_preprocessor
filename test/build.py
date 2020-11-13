import numpy as np
import pandas as pd
import toml
from clean import *
from encoders.index import encoder_selector


def build(config):
    df = clean_dataframe(
        get_dataframe(config['data']), config['dataframe'])
    return df


config = toml.load("test/config.toml")
print(build(config).head())
