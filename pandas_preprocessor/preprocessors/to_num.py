import pandas as pd
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class ToNum(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        ty = self.settings.get('type')
        dataframe[self.column] = pd.to_numeric(
            dataframe[self.column], downcast=ty)
        # Look into using the below
        # convert just columns "a" and "b"
        # df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
        return dataframe

    def invert_transform(self, dataframe):
        ty = self.settings.get('invert_type')
        if(ty is not None):
            dataframe[self.column] = dataframe[self.column].astype(ty)
        return dataframe
