from pandas_preprocessor.processors.encoders import *
from pandas_preprocessor.processors.preprocessors import *


def processor_selector(algoName):
    return encoders.get(algoName, preprocessor_selector.get(algoName))
