from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd

# NOTE: invert_transform not supported


class Binarizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.Binarizer(
            threshold=self.settings.get('threshold', 0.0),
            copy=self.settings.get('copy', True)
        )

    def transform(self, dataframe):
        x = self.encoder.transform(dataframe[self.column].to_frame())
        dataframe[self.column] = x
        return dataframe
