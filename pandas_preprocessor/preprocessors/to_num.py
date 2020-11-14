import pandas as pd


class ToNum(object):

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings if settings is not None else {}

    def transform(self, dataframe):
        ty = self.settings.get('type')
        dataframe[self.column] = pd.to_numeric(
            dataframe[self.column], downcast=ty)
        return dataframe

    def invert_transform(self, dataframe):
        ty = self.settings.get('invert_type')
        if(ty is None):
            return dataframe
        else:
            dataframe[self.column] = dataframe[self.column].astype(ty)
            return dataframe
