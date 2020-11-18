import joblib


class AEncoder(object):
    """
    A class to be inherited in order to make an encoder
    """

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings if settings is not None else {}
        self.encoder = None

    def transform(self, dataframe):
        return dataframe

    def invert_transform(self, dataframe):
        return dataframe

    def pickle_process(self, dataframe, get_column_fn=lambda df, c: df[c].to_frame()):
        joblib_file = self.settings.get('file_location')
        if(self.settings.get('is_use_case', False)):
            self.encoder = joblib.load(joblib_file)
        else:
            c = get_column_fn(dataframe, self.column)
            self.encoder.fit(c)
            if(joblib_file is not None):
                joblib.dump(self.encoder, joblib_file)
