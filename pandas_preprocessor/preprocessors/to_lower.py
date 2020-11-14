from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class ToLower(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda string: string.lower())
        return dataframe
