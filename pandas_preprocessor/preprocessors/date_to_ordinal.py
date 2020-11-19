from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
import datetime


class DateToOrdinal(APreprocessor):

    def __init__(self, column, dataframe, settings):
        APreprocessor.__init__(self, column, dataframe, settings)
        print(self.settings)

    def transform(self, dataframe):
        def to_date(date_time_str):
            date_time_obj = datetime.datetime.strptime(
                date_time_str, self.settings['date_format'])
            return date_time_obj

        def to_ordinal(date_time_obj):
            return date_time_obj.toordinal()

        dataframe[self.column] = dataframe[self.column].map(
            to_date).map(to_ordinal)
        return dataframe

    def invert_transform(self, dataframe):
        def from_date(date_time_obj):
            return date_time_obj.strftime(self.settings['date_format'])

        def from_ordinal(ordinal):
            return datetime.date.fromordinal(ordinal)

        dataframe[self.column] = dataframe[self.column].map(
            from_ordinal).map(from_date)
        return dataframe
