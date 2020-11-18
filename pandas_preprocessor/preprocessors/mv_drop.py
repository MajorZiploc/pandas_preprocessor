from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

# NOTE: invert_transform not supported


class MvDrop(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        if(self.settings.get('is_use_case', False)):
            df = dataframe[dataframe[self.column].notnull()]
        return df
