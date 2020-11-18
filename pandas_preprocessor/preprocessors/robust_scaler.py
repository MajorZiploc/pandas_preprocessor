from sklearn import preprocessing
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class RobustScaler(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.scaler = preprocessing.RobustScaler(
            with_centering=settings.get('with_centering', True),
            with_scaling=settings.get('with_scaling', True),
            quantile_range=settings.get(
                'quantile_range', tuple([25.0, 75.0])),
            copy=settings.get('copy', True)
        )
        self.pickle_process(dataframe)

    def transform(self, dataframe):
        dataframe[self.column] = self.scaler.transform(
            dataframe[self.column].to_frame())
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.scaler.inverse_transform(
            dataframe[self.column].to_frame())
        return dataframe
