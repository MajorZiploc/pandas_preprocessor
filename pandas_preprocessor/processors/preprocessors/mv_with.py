from pandas_preprocessor.processors.preprocessors.apreprocessor import APreprocessor


class MvWith(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].fillna(
            self.settings.get('value'))
        return dataframe

    def invert_transform(self, dataframe):
        return dataframe
