from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class MvMode(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.mode = dataframe[self.column].mode()[0]

    def transform(self, dataframe):
        if(not self.settings.get('is_use_case', False)):
            dataframe[self.column] = dataframe[self.column].fillna(self.mode)
        return dataframe
