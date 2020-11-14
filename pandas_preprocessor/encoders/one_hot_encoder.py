from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd


class OneHotEncoder(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.og_column = None
        self.added_columns = []
        self.shouldTrackInvert = self.settings.get('should_track_invert', True)

    def transform(self, dataframe):
        cs = pd.get_dummies(
            dataframe[self.column], prefix=self.column)
        if(self.shouldTrackInvert):
            for c in cs.columns:
                self.added_columns.append(c)
            self.og_column = dataframe[self.column]
        dataframe = pd.concat([dataframe, cs], axis=1)
        dataframe.drop(self.column, inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        if(self.shouldTrackInvert):
            dataframe[self.column] = self.og_column
            dataframe.drop(self.added_columns, inplace=True, axis=1)
        return dataframe
