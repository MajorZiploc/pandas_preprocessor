from sklearn import preprocessing
from pandas_preprocessor.processors.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class Normalize(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.min_max_scaler = preprocessing.MinMaxScaler()
        print(dataframe.head())
        self.min_max_scaler.fit(dataframe[self.column].to_frame())

    def transform(self, dataframe):
        dataframe[self.column] = self.min_max_scaler.transform(
            dataframe[self.column].to_frame())
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.min_max_scaler.inverse_transform(
            dataframe[self.column].to_frame())
        return dataframe
