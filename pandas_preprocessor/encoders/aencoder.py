import joblib


class AEncoder(object):

    def __init__(self, column, dataframe, settings):
        self.column = column
        self.settings = settings if settings is not None else {}
        self.encoder = None

    def transform(self, dataframe):
        return dataframe

    def invert_transform(self, dataframe):
        return dataframe

    def pickle_process(self, dataframe):
        joblib_file = self.settings.get('file_location')
        if(self.settings.get('is_use_case', False)):
            self.encoder = joblib.load(joblib_file)
        else:
            c = dataframe[self.column].to_frame()
            self.encoder.fit(c)
            if(joblib_file is not None):
                joblib.dump(self.encoder, joblib_file)
