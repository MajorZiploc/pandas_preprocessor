from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd
import joblib


class LabelBinarizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.LabelBinarizer()
        c = dataframe[self.column].to_frame()
        self.encoder.fit(c)
        joblib_file = settings.get('file_location')
        if(joblib_file is not None):
            joblib.dump(self.encoder, joblib_file)

    def transform(self, dataframe):
        x = self.encoder.transform(dataframe[self.column].to_frame())
        cs = pd.DataFrame(self.encoder.transform(dataframe[self.column]))\
            .add_prefix(self.column+"_")
        dataframe = dataframe.join(cs)
        dataframe.drop(self.column, inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        binCols = dataframe.filter(regex='^'+self.column+'_', axis=1)
        x = self.encoder.inverse_transform(
            binCols.to_numpy())
        binDf = pd.DataFrame(x).rename({0: self.column}, axis=1)
        dataframe.drop(binCols, inplace=True, axis=1)
        dataframe = dataframe.join(binDf)
        return dataframe
