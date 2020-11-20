from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import re


class Suffix(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        self.value = self.settings.get('value', '')

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda e: e + self.value)
        return dataframe

    def invert_transform(self, dataframe):
        def r(s):
            return re.sub(r'' + self.value + '$', '', s)
        dataframe[self.column] = dataframe[self.column].map(r)
        return dataframe
