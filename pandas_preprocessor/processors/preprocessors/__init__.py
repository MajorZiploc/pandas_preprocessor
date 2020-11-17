from pandas_preprocessor.processors.preprocessors.substitution import Substitution
from pandas_preprocessor.processors.preprocessors.to_num import ToNum
from pandas_preprocessor.processors.preprocessors.to_type import ToType
from pandas_preprocessor.processors.preprocessors.apreprocessor import APreprocessor
from pandas_preprocessor.processors.preprocessors.to_lower import ToLower
from pandas_preprocessor.processors.preprocessors.to_upper import ToUpper
from pandas_preprocessor.processors.preprocessors.mv_mode import MvMode
from pandas_preprocessor.processors.preprocessors.mv_with import MvWith
from pandas_preprocessor.processors.preprocessors.mv_mean import MvMean
from pandas_preprocessor.processors.preprocessors.mv_median import MvMedian
from pandas_preprocessor.processors.preprocessors.normalize import Normalize

preprocessors = {
    'substitution': lambda column, dataframe, settings: Substitution(column, dataframe, settings),
    'to_num': lambda column, dataframe, settings: ToNum(column, dataframe, settings),
    'to_type': lambda column, dataframe, settings: ToType(column, dataframe, settings),
    'to_lower': lambda column, dataframe, settings: ToLower(column, dataframe, settings),
    'to_upper': lambda column, dataframe, settings: ToUpper(column, dataframe, settings),
    'mv_mode': lambda column, dataframe, settings: MvMode(column, dataframe, settings),
    'mv_with': lambda column, dataframe, settings: MvWith(column, dataframe, settings),
    'mv_mean': lambda column, dataframe, settings: MvMean(column, dataframe, settings),
    'mv_median': lambda column, dataframe, settings: MvMedian(column, dataframe, settings),
    'normalize': lambda column, dataframe, settings: Normalize(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
