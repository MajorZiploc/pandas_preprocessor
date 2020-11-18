from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

# NOTE: invert_transform not supported


class MvMean(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        x = dataframe[self.column].mean()
        dataframe[self.column] = dataframe[self.column].fillna(x)
        return dataframe
