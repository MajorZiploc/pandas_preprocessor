from pandas_preprocessor.encoders.label_encoder import LabelEncoder
from pandas_preprocessor.encoders.label_binarizer import LabelBinarizer
from pandas_preprocessor.encoders.kbins_discretizer import KBinsDiscretizer

encoders = {
    'label_encoder': lambda column, dataframe, settings: LabelEncoder(column, dataframe, settings),
    'label_binarizer': lambda column, dataframe, settings: LabelBinarizer(column, dataframe, settings),
    'kbins_discretizer': lambda column, dataframe, settings: KBinsDiscretizer(column, dataframe, settings)
}


def add_encoder(algoName, encoder_supplier):
    if (algoName not in encoders):
        encoders[algoName] = encoder_supplier
    else:
        raise Exception(
            '%s is already an encoder. Try using a different name. Here is a list of existing encoders: %s'
            % (algoName, [k for k in encoders.keys()])
        )


def encoder_selector(algoName):
    try:
        return encoders[algoName]
    except KeyError:
        raise KeyError(
            '%s is not an available encoder. Here is a list of available preprocessors: %s'
            % (algoName, [k for k in encoders.keys()])
        )
