from sklearn import preprocessing
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class QuantileTransformer(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.scaler = preprocessing.QuantileTransformer(
            n_quantiles=settings.get('n_quantiles', 1000),
            output_distribution=settings.get('output_distribution', 'uniform'),
            ignore_implicit_zeros=settings.get(
                'ignore_implicit_zeros', False),
            subsample=settings.get(
                'subsample', 100000),
            random_state=settings.get(
                'random_state', None),
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
