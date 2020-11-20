from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import pandas as pd


class JoinColumns(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)

    def transform(self, dataframe):
        on = self.settings.get('on', '')
        dataframe[self.settings['new_column']] = dataframe[self.column]\
            .map(lambda s: s + on).str.cat(dataframe[self.settings['other_column']])
        if(self.settings.get('should_drop_original', True)):
            dataframe.drop(self.column, inplace=True, axis=1)
            dataframe.drop(self.settings['other_column'], inplace=True, axis=1)
        return dataframe

    def invert_transform(self, dataframe):
        on = self.settings.get('on')
        if(on is not None):
            def f(x):
                d = pd.Series(str(x).split(on, 1))
                return d

            dataframe[[self.column, self.settings['other_column']]
                      ] = dataframe[self.settings['new_column']]\
                .apply(lambda x: pd.Series(str(x).split(on, 1)))
            dataframe.drop(self.settings['new_column'], inplace=True, axis=1)
        return dataframe
