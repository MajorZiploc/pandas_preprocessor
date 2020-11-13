import re


class Substitution(object):

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings

    def transform(self, dataframe):
        dataframe[self.column] = dataframe[self.column].map(
            lambda string: re.sub(self.settings['pattern'], self.settings['replace'], string, flags=re.I))
        return dataframe

    def invert_transform(self, dataframe):
        p = self.settings.get('invert_pattern')
        r = self.settings.get('invert_replace')
        if(p is not None and r is not None):
            dataframe[self.column] = dataframe[self.column].map(
                lambda string: re.sub(p, r, string, flags=re.I))
            return dataframe
        else:
            return dataframe
