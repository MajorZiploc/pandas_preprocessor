from sklearn import preprocessing
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd

# NOTE: invert_transform not supported


class PolynomialFeatures(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.scaler = preprocessing.PolynomialFeatures(
            degree=self.settings.get('degree', 2),
            interaction_only=self.settings.get('interaction_only', False),
            include_bias=self.settings.get(
                'include_bias', True),
            order=self.settings.get(
                'order', 'C')
        )
        self.pickle_process(dataframe)

    def transform(self, dataframe):
        dataframe[self.column] = self.scaler.transform(
            dataframe[self.column].to_frame())
        return dataframe
