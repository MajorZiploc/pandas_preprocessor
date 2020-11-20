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
from pandas_preprocessor.preprocessors.polynomial_features import PolynomialFeatures
from pandas_preprocessor.preprocessors.mv_drop import MvDrop
from pandas_preprocessor.preprocessors.date_to_ordinal import DateToOrdinal
from pandas_preprocessor.preprocessors.abs import Abs
from pandas_preprocessor.preprocessors.add import Add
from pandas_preprocessor.preprocessors.mult import Mult
from pandas_preprocessor.preprocessors.div_by import DivBy
from pandas_preprocessor.preprocessors.ltrim import LTrim
from pandas_preprocessor.preprocessors.rtrim import RTrim
from pandas_preprocessor.preprocessors.trim import Trim
from pandas_preprocessor.preprocessors.prefix import Prefix
from pandas_preprocessor.preprocessors.suffix import Suffix
from pandas_preprocessor.preprocessors.keep import Keep

preprocessors = {
    'substitution': Substitution,
    'to_num': ToNum,
    'to_type': ToType,
    'to_lower': ToLower,
    'to_upper': ToUpper,
    'mv_mode': MvMode,
    'mv_with': MvWith,
    'mv_mean': MvMean,
    'mv_median': MvMedian,
    'min_max_scaler': MinMaxScaler,
    'standard_scaler': StandardScaler,
    'binarizer': Binarizer,
    'normalizer': Normalizer,
    'max_abs_scaler': MaxAbsScaler,
    'robust_scaler': RobustScaler,
    'power_transformer': PowerTransformer,
    'quantile_transformer': QuantileTransformer,
    'polynomial_features': PolynomialFeatures,
    'mv_drop': MvDrop,
    'date_to_ordinal': DateToOrdinal,
    'abs': Abs,
    'add': Add,
    'mult': Mult,
    'div_by': DivBy,
    'ltrim': LTrim,
    'rtrim': RTrim,
    'trim': Trim,
    'prefix': Prefix,
    'suffix': Suffix,
    'keep': Keep
}


def add_preprocessor(algo_name, preprocessor_supplier):
    if (algo_name not in preprocessors):
        preprocessors[algo_name] = preprocessor_supplier
    else:
        raise Exception(
            '%s is already an encoder. Try using a different name. Here is a list of existing encoders: %s'
            % (algo_name, [k for k in preprocessors.keys()])
        )


def preprocessor_selector(algo_name):
    try:
        return preprocessors[algo_name]
    except KeyError:
        raise KeyError(
            '%s is not an available preprocessor. Here is a list of available preprocessors: %s'
            % (algo_name, [k for k in preprocessors.keys()])
        )
