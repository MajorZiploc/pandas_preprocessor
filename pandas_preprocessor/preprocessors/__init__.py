from pandas_preprocessor.preprocessors.substitution import Substitution

preprocessors = {
    'substitution': lambda column, dataframe, settings: Substitution(column, dataframe, settings)
}


def preprocessor_selector(algoName):
    return preprocessors.get(algoName)
