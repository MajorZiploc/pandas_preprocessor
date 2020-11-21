from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class MvDrop(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        if(not self.settings.get('is_use_case', False)):
            dataframe = dataframe[dataframe[self.column].notnull()]
        return dataframe
