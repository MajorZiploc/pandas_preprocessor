from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor


class RenameColumn(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        dataframe.rename(
            columns={self.column: self.settings['value']}, inplace=True)
        return dataframe

    def invert_transform(self, dataframe):
        dataframe.rename(
            columns={self.settings['value']: self.column}, inplace=True)
        return dataframe
