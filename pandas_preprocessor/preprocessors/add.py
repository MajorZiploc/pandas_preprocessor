from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class Add(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.value = self.settings.get('value', 0)

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda e: e + self.value)
        print(dataframe.head())
        return dataframe

    def invert_transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda e: e - self.value)
        return dataframe
