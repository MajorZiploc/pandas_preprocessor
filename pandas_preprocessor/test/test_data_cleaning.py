from build import *
import toml
import pandas as pd
import os
import numpy as np

this_dir = os.path.dirname(os.path.realpath(__file__))


def test_keeprows():
    tomlLoc = os.path.join(this_dir, "keeprows_test.toml")
    config = toml.load(tomlLoc)
    fileLoc = os.path.join(this_dir, config['data']['connectionstring'])
    config['data']['connectionstring'] = fileLoc
    df = get_dataframe(config['data'])
    cleaned_df = clean_dataframe(df, config['dataframe'])
    actualRows = cleaned_df.columns.to_numpy()
    expectedRows = np.array(['Name', 'Number', 'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice',
                             'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock',
                             'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy'])
    assert pd.DataFrame.equals(expectedRows, actualRows)
