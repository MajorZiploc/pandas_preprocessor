from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder


class LabelEncoder(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.LabelEncoder()
        self.pickle_process(dataframe)

    def transform(self, dataframe):
        dataframe[self.column] = self.encoder.transform(
            dataframe[self.column])
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.encoder.inverse_transform(
            dataframe[self.column])
        return dataframe
