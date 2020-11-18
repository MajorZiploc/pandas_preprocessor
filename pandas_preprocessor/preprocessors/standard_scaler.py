from sklearn import preprocessing
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class StandardScaler(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.scaler = preprocessing.StandardScaler(
            copy=self.settings.get('copy', True),
            with_mean=self.settings.get('with_mean', True),
            with_std=self.settings.get('with_std', True),
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
