from pandas_preprocessor.preprocessors.substitution import Substitution
from pandas_preprocessor.preprocessors.to_num import ToNum
from pandas_preprocessor.preprocessors.to_type import ToType
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
from pandas_preprocessor.preprocessors.to_lower import ToLower
from pandas_preprocessor.preprocessors.to_upper import ToUpper
from pandas_preprocessor.preprocessors.mv_mode import MvMode

preprocessors = {
    'substitution': lambda column, dataframe, settings: Substitution(column, dataframe, settings),
    'to_num': lambda column, dataframe, settings: ToNum(column, dataframe, settings),
    'to_type': lambda column, dataframe, settings: ToType(column, dataframe, settings),
    'to_lower': lambda column, dataframe, settings: ToLower(column, dataframe, settings),
    'to_upper': lambda column, dataframe, settings: ToUpper(column, dataframe, settings),
    'mv_mode': lambda column, dataframe, settings: MvMode(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
