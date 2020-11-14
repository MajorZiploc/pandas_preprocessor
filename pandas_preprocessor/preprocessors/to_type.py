import pandas as pd
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class ToType(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        ty = self.settings.get('type')
        if(ty is None):
            return dataframe
        else:
            dataframe[self.column] = dataframe[self.column].astype(ty)
            return dataframe

    def invert_transform(self, dataframe):
        ty = self.settings.get('invert_type')
        if(ty is None):
            return dataframe
        else:
            dataframe[self.column] = dataframe[self.column].astype(ty)
            return dataframe
