from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import joblib


class LabelEncoder(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.labelEncoder = preprocessing.LabelEncoder()
        self.labelEncoder.fit(dataframe[self.column])
        joblib_file = settings.get('file_location')
        if(joblib_file is not None):
            joblib.dump(self.labelEncoder, joblib_file)

    def transform(self, dataframe):
        dataframe[self.column] = self.labelEncoder.transform(
            dataframe[self.column])
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.labelEncoder.inverse_transform(
            dataframe[self.column])
        return dataframe
