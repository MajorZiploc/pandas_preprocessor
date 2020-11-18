from pandas_preprocessor.preprocessors.substitution import Substitution
from pandas_preprocessor.preprocessors.to_num import ToNum
from pandas_preprocessor.preprocessors.to_type import ToType
from pandas_preprocessor.preprocessors.apreprocessor import APreprocessor
from pandas_preprocessor.preprocessors.to_lower import ToLower
from pandas_preprocessor.preprocessors.to_upper import ToUpper
from pandas_preprocessor.preprocessors.mv_mode import MvMode
from pandas_preprocessor.preprocessors.mv_with import MvWith
from pandas_preprocessor.preprocessors.mv_mean import MvMean
from pandas_preprocessor.preprocessors.mv_median import MvMedian
from pandas_preprocessor.preprocessors.min_max_scaler import MinMaxScaler
from pandas_preprocessor.preprocessors.standardize import Standardize
from pandas_preprocessor.preprocessors.binarizer import Binarizer
from pandas_preprocessor.preprocessors.normalizer import Normalizer
from pandas_preprocessor.preprocessors.max_abs_scaler import MaxAbsScaler

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
    'min_max_scaler': lambda column, dataframe, settings: MinMaxScaler(column, dataframe, settings),
    'standardize': lambda column, dataframe, settings: Standardize(column, dataframe, settings),
    'binarizer': lambda column, dataframe, settings: Binarizer(column, dataframe, settings),
    'normalizer': lambda column, dataframe, settings: Normalizer(column, dataframe, settings),
    'max_abs_scaler': lambda column, dataframe, settings: MaxAbsScaler(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
