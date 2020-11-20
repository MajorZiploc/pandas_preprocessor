from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

# NOTE: invert_transform not supported


class MvWith(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        if(not self.settings.get('is_use_case', False)):
            dataframe[self.column] = dataframe[self.column].fillna(
                self.settings.get('value'))
        return dataframe
