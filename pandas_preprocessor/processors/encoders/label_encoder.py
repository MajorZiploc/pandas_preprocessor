from sklearn import preprocessing
from pandas_preprocessor.processors.encoders.aencoder import AEncoder
import joblib


class LabelEncoder(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.LabelEncoder()
        joblib_file = settings.get('file_location')
        if(self.settings.get('is_use_case', False)):
            self.encoder = joblib.load(joblib_file)
        else:
            self.encoder.fit(dataframe[self.column])
            if(joblib_file is not None):
                joblib.dump(self.encoder, joblib_file)

    def transform(self, dataframe):
        dataframe[self.column] = self.encoder.transform(
            dataframe[self.column])
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.encoder.inverse_transform(
            dataframe[self.column])
        return dataframe
