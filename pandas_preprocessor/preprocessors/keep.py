from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import re


class Keep(APreprocessor):
    """
    NOTE: invert_transform not supported
    """

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        def pred(row):
            b = re.search(
                self.settings['pattern'], row[self.column], flags=self.settings.get('flags', 0))\
                is not None
            return b
        if(not self.settings.get('is_use_case', False)):
            dataframe = dataframe[dataframe.apply(pred, axis=1)]
        return dataframe
