from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd
import joblib


class LabelBinarizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.labelBinarizer = preprocessing.LabelBinarizer()
        self.labelBinarizer.fit(dataframe[self.column].to_frame())
        joblib_file = settings.get('file_location')
        if(joblib_file is not None):
            joblib.dump(self.labelBinarizer, joblib_file)

    def transform(self, dataframe):
        x = self.labelBinarizer.transform(dataframe[self.column].to_frame())
        cs = pd.DataFrame(self.labelBinarizer.transform(dataframe[self.column]))\
            .add_prefix(self.column+"_")
        dataframe = pd.concat([dataframe, cs], axis=1)
        dataframe.drop(self.column, inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        waterCols = dataframe.filter(regex='^'+self.column+'_', axis=1)
        x = self.labelBinarizer.inverse_transform(
            waterCols.to_numpy())
        waterDf = pd.DataFrame(x).rename({0: self.column}, axis=1)
        dataframe.drop(waterCols, inplace=True, axis=1)
        dataframe = pd.merge(dataframe, waterDf,
                             left_index=True, right_index=True)
        return dataframe
