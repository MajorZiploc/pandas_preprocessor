from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class Trim(APreprocessor):

    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        def s(e):
            return e.strip()

        dataframe[self.column] = dataframe[self.column].map(s)
        return dataframe
