from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

# NOTE: invert_transform not supported


class MvDrop(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        df = dataframe[dataframe[self.column].notnull()]
        print('mv_drop')
        print(df.head())
        # c = dataframe[[self.column]]
        # print(c.head())
        # dataframe.drop(self.column, inplace=True, axis=1)
        # c = c.dropna(axis=0, how='any', thresh=None, subset=None)
        # dataframe = dataframe.join(c)
        # print(dataframe.head())
        return df
