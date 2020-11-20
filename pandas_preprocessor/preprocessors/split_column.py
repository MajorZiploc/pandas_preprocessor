from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class SplitColumn(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        on = self.settings.get('on', ' ')

        def f(x):
            d = pd.Series(str(x).split(on, 1))
            return d

        dataframe[[self.settings['column1'], self.settings['column2']]
                  ] = dataframe[self.column]\
            .apply(lambda x: pd.Series(str(x).split(on, 1)))
        if(self.settings.get('should_drop_original', True)):
            dataframe.drop(self.column, inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        on = self.settings.get('on', ' ')
        dataframe[self.column] = dataframe[self.settings['column1']]\
            .map(lambda s: s + on).str.cat(dataframe[self.settings['column2']])
        dataframe.drop(self.settings['column1'], inplace=True, axis=1)
        dataframe.drop(self.settings['column2'], inplace=True, axis=1)
        return dataframe
