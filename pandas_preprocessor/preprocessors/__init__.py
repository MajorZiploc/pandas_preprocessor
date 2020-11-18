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
from pandas_preprocessor.preprocessors.standard_scaler import StandardScaler
from pandas_preprocessor.preprocessors.binarizer import Binarizer
from pandas_preprocessor.preprocessors.normalizer import Normalizer
from pandas_preprocessor.preprocessors.max_abs_scaler import MaxAbsScaler
from pandas_preprocessor.preprocessors.robust_scaler import RobustScaler
from pandas_preprocessor.preprocessors.power_transformer import PowerTransformer
from pandas_preprocessor.preprocessors.quantile_transformer import QuantileTransformer

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
    'standard_scaler': lambda column, dataframe, settings: StandardScaler(column, dataframe, settings),
    'binarizer': lambda column, dataframe, settings: Binarizer(column, dataframe, settings),
    'normalizer': lambda column, dataframe, settings: Normalizer(column, dataframe, settings),
    'max_abs_scaler': lambda column, dataframe, settings: MaxAbsScaler(column, dataframe, settings),
    'robust_scaler': lambda column, dataframe, settings: RobustScaler(column, dataframe, settings),
    'power_transformer': lambda column, dataframe, settings: PowerTransformer(column, dataframe, settings),
    'quantile_transformer': lambda column, dataframe, settings: QuantileTransformer(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
