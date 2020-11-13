from pandas_preprocessor.encoders.label_encoder import LabelEncoder

encoders = {
    'label_encoding': lambda column, dataframe, settings: LabelEncoder(column, dataframe, settings)
}


def encoder_selector(algoName):
    return encoders.get(algoName)
