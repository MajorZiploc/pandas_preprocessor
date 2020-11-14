import pandas as pd


class ToType(object):

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings if settings is not None else {}

    def transform(self, dataframe):
        ty = self.settings.get('type')
        if(ty is None):
            return dataframe
        else:
            dataframe[self.column] = dataframe[self.column].astype(ty)
            return dataframe

    def invert_transform(self, dataframe):
        ty = self.settings.get('invert_type')
        if(ty is None):
            return dataframe
        else:
            dataframe[self.column] = dataframe[self.column].astype(ty)
            return dataframe
