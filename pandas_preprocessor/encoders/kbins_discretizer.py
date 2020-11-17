from sklearn import preprocessing
from pandas_preprocessor.encoders.aencoder import AEncoder
import pandas as pd


class KBinsDiscretizer(AEncoder):

    def __init__(self, column, dataframe, settings):
        AEncoder.__init__(self, column, dataframe, settings)
        self.encoder = preprocessing.KBinsDiscretizer(
            n_bins=self.settings.get('n_bins', 5),
            encode=self.settings.get('encode', 'onehot'),
            strategy=self.settings.get('strategy', 'quantile')
        )
        self.pickle_process(dataframe)

    def transform(self, dataframe):
        x = self.encoder.transform(dataframe[[self.column]])
        cs = pd.DataFrame(x.toarray())\
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
            binCols)
        binDf = pd.DataFrame(x).rename({0: self.column}, axis=1)
        dataframe.drop(binCols, inplace=True, axis=1)
        dataframe = dataframe.join(binDf)
        return dataframe
