import re
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
from pandas_preprocessor.utils import str_flags_to_regex_flags


class Substitution(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        def fnWithFlags(string):
            flags = self.settings.get('flags').lower()
            return re.sub(self.settings['pattern'], self.settings['replace'], string, flags=str_flags_to_regex_flags(flags))

        def fnWithoutFlags(string):
            return re.sub(self.settings['pattern'], self.settings['replace'], string)

        fn = fnWithFlags if self.settings.get('flags') else fnWithoutFlags

        flags = self.settings.get('flags')
        dataframe[self.column] = dataframe[self.column].map(fn)
        return dataframe

    def invert_transform(self, dataframe):
        p = self.settings.get('invert_pattern')
        r = self.settings.get('invert_replace')
        if(p is not None and r is not None):
            dataframe[self.column] = dataframe[self.column].map(
                lambda string: re.sub(p, r, string, flags=re.I))
        return dataframe
