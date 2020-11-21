from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class DropColumn(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        dataframe.drop(self.column, axis=1, inplace=True)
        return dataframe
