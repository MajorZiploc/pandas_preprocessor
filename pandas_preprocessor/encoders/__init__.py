from pandas_preprocessor.encoders.label_encoder import LabelEncoder
from pandas_preprocessor.encoders.one_hot_encoder import OneHotEncoder
from pandas_preprocessor.encoders.label_binarizer import LabelBinarizer

encoders = {
    'label_encoding': lambda column, dataframe, settings: LabelEncoder(column, dataframe, settings),
    'one_hot_encoding': lambda column, dataframe, settings: OneHotEncoder(column, dataframe, settings),
    'label_binarizer': lambda column, dataframe, settings: LabelBinarizer(column, dataframe, settings)
}


def encoder_selector(algoName):
    return encoders.get(algoName)
