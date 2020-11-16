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
        x = self.encoder.transform(dataframe[self.column])
        cs = pd.DataFrame(x)\
            .add_prefix(self.column+"_")
        cs.shape
        indices = [i for i in range(0, len(cs.index))]
        joinColumn = '___labelbinarizer__index__join_column___'
        dataframe[joinColumn] = indices
        # for (columnName, columnData) in cs.iteritems():
        #     cs[columnName] = pd.to_numeric(
        #         cs[columnName], downcast='integer')

# the problem is that the indexs of the dataframes dont match.
        dataframe = dataframe.join(cs, how='inner', on=joinColumn)
        # dataframe = pd.concat([dataframe, cs], axis=1)
        dataframe.drop(self.column, inplace=True, axis=1)
        dataframe.drop(joinColumn, inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        binCols = dataframe.filter(regex='^'+self.column+'_', axis=1)
        x = self.encoder.inverse_transform(
            binCols.to_numpy())
        binDf = pd.DataFrame(x).rename({0: self.column}, axis=1)
        dataframe.drop(binCols, inplace=True, axis=1)
        dataframe = dataframe.join(binDf)
        return dataframe
