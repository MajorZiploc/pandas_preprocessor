from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class DivBy(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.value = self.settings.get('value', 1)

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda e: e / self.value)
        return dataframe
