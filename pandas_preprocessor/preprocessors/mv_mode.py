from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

# NOTE: invert_transform not supported


class MvMode(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        if(not self.settings.get('is_use_case', False)):
            x = dataframe[self.column].mode()[0]
            dataframe[self.column] = dataframe[self.column].fillna(x)
        return dataframe
