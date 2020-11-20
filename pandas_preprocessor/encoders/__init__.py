from pandas_preprocessor.encoders.label_encoder import LabelEncoder
from pandas_preprocessor.encoders.label_binarizer import LabelBinarizer
from pandas_preprocessor.encoders.kbins_discretizer import KBinsDiscretizer

encoders = {
    'label_encoder': LabelEncoder,
    'label_binarizer': LabelBinarizer,
    'kbins_discretizer': KBinsDiscretizer
}


def add_encoder(algo_name, encoder_supplier):
    if (algo_name not in encoders):
        encoders[algo_name] = encoder_supplier
    else:
        raise Exception(
            '%s is already an encoder. Try using a different name. Here is a list of existing encoders: %s'
            % (algo_name, [k for k in encoders.keys()])
        )


def encoder_selector(algo_name):
    try:
        return encoders[algo_name]
    except KeyError:
        raise KeyError(
            '%s is not an available encoder. Here is a list of available preprocessors: %s'
            % (algo_name, [k for k in encoders.keys()])
        )
