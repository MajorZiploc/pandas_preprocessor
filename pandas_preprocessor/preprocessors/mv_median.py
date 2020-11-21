from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class MvMedian(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.median = dataframe[self.column].median()

    def transform(self, dataframe):
        if(not self.settings.get('is_use_case', False)):
            dataframe[self.column] = dataframe[self.column].fillna(self.median)
        return dataframe
