from pandas_preprocessor.processors.preprocessors.apreprocessor import APreprocessor


class MvMean(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        x = dataframe[self.column].mean()
        dataframe[self.column] = dataframe[self.column].fillna(x)
        return dataframe

    def invert_transform(self, dataframe):
        return dataframe
