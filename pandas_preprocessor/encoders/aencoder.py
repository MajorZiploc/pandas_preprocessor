
class AEncoder(object):

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings if settings is not None else {}

    def transform(self, dataframe):
        pass

    def invert_transform(self, dataframe):
        return dataframe
