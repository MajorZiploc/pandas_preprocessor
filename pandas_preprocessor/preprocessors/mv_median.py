from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class MvMedian(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        x = dataframe[self.column].median()
        dataframe[self.column] = dataframe[self.column].fillna(x)
        return dataframe

    def invert_transform(self, dataframe):
        return dataframe
