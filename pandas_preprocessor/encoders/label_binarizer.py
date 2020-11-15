from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd
import joblib


class LabelBinarizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.labelBinarizer = preprocessing.LabelBinarizer(neg_label=0)
        self.labelBinarizer.fit(dataframe[self.column].to_frame())
        joblib_file = settings.get('file_location')
        if(joblib_file is not None):
            joblib.dump(self.labelBinarizer, joblib_file)

    def transform(self, dataframe):
        x = self.labelBinarizer.transform(dataframe[self.column].to_frame())
        cs = self.labelBinarizer.transform(dataframe[self.column])
        dataframe = pd.concat([dataframe, pd.DataFrame(cs)], axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        # dataframe[self.column] = self.labelBinarizer.inverse_transform(
        #     dataframe[self.column])
        return dataframe
