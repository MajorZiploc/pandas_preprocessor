from sklearn import preprocessing


class LabelEncoder(object):

    def __init__(self, column, dataframe, settings):
        self.labelEncoder = preprocessing.LabelEncoder()
        self.column = column
        self.set_label_encoder(dataframe)

    def set_label_encoder(self, dataframe):
        self.labelEncoder.fit(dataframe[self.column])

    def label_encode_transform(self, dataframe):
        dataframe[self.column] = self.labelEncoder.transform(
            dataframe[self.column])
        return dataframe

    def label_encode_inverse_transform(self, dataframe):
        dataframe[self.column] = self.labelEncoder.inverse_transform(
            dataframe[self.column])
        return dataframe

    def transform(self, dataframe):
        return self.label_encode_transform(dataframe)

    def invert_transform(self, dataframe):
        return self.label_encode_inverse_transform(dataframe)