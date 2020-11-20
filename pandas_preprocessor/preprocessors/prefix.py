from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import re


class Prefix(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.value = self.settings.get('value', 0)

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda e: self.value + e)
        return dataframe

    def invert_transform(self, dataframe):
        def r(s):
            return re.sub(r'^' + self.value, '', s)
        dataframe[self.column] = dataframe[self.column].map(r)
        return dataframe
