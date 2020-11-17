from sklearn import preprocessing
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd
import joblib


class NormalizeMinMaxScaler(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.scaler = preprocessing.MinMaxScaler()
        joblib_file = settings.get('file_location')
        if(self.settings.get('is_use_case', False)):
            self.scaler = joblib.load(joblib_file)
        else:
            c = dataframe[self.column].to_frame()
            self.scaler.fit(c)
            if(joblib_file is not None):
                joblib.dump(self.scaler, joblib_file)

    def transform(self, dataframe):
        dataframe[self.column] = self.scaler.transform(
            dataframe[self.column].to_frame())
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = self.scaler.inverse_transform(
            dataframe[self.column].to_frame())
        return dataframe
