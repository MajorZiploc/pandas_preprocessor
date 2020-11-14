from pandas_preprocessor.preprocessors.substitution import Substitution
from pandas_preprocessor.preprocessors.to_num import ToNum
from pandas_preprocessor.preprocessors.to_type import ToType
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor

preprocessors = {
    'substitution': lambda column, dataframe, settings: Substitution(column, dataframe, settings),
    'to_num': lambda column, dataframe, settings: ToNum(column, dataframe, settings),
    'to_type': lambda column, dataframe, settings: ToType(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
