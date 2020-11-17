from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd


class LabelBinarizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.LabelBinarizer(
            neg_label=settings.get('neg_label', 0),
            pos_label=settings.get('pos_label', 1),
            sparse_output=settings.get('sparse_output', False)
        )
        self.pickle_process(dataframe)

    def transform(self, dataframe):
        x = self.encoder.transform(dataframe[self.column])
        cs = pd.DataFrame(x)\
            .add_prefix(self.column+"_")
        # the problem is that the indexs of the dataframes dont match.
        # the join column gets around it
        indices = [i for i in range(0, len(cs.index))]
        joinColumn = '___labelbinarizer__index__join_column___'
        dataframe[joinColumn] = indices

        dataframe = dataframe.join(cs, how='inner', on=joinColumn)
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
