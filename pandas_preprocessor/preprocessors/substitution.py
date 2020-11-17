import re
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
from functools import reduce


class Substitution(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

        self.flag_map = {
            "i": re.IGNORECASE,
            "x": re.VERBOSE,
            "m": re.MULTILINE,
            "s": re.DOTALL,
            "u": re.UNICODE,
            "l": re.LOCALE,
            "d": re.DEBUG,
            "a": re.ASCII,
            "t": re.TEMPLATE
        }

    def transform(self, dataframe):
        def fnWithFlags(string):
            def r(acc, ele):
                acc = acc | ele
                return acc
            flags = self.settings.get('flags').lower()
            return re.sub(self.settings['pattern'], self.settings['replace'], string, flags=reduce(r, [self.flag_map[f] for f in flags]))

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
