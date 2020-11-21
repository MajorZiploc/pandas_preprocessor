from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class MvMean(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        if(not settings.get('is_use_case', False)):
            x = dataframe[self.column].mean()
            dataframe[self.column] = dataframe[self.column].fillna(x)
        return dataframe
