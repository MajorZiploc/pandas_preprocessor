import pandas as pd
from pandas_preprocessor.utils import *
from pandas_preprocessor.preprocessors import *
from pandas_preprocessor.encoders import *


def get_dataframe(dataConfig):
    return pd.read_csv(dataConfig['connectionstring']) if dataConfig['format'] == 'csv' \
        else None


def encodersAction(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        for step in es:
            df = encoderAction(df, step, column)
    return df


def encoderAction(df, step, column):
    setEncoder(df, step, column)
    return encoderTransform(df, step)


def setEncoder(df, step, column):
    if(step is not None):
        step['encoder'] = encoder_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def encoderTransform(df, step):
    if(step is not None):
        df = step['encoder'].transform(df)
    return df


def encodersInvert(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        for step in reversed(es):
            df = encoderInvert(df, step)
    return df


def encoderInvert(df, step):
    if(step is not None):
        df = step['encoder'].invert_transform(df)
    return df


def preprocessorsAction(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        for step in ps:
            df = preprocessorAction(df, step, column)
    return df


def preprocessorAction(df, step, column):
    setPreprocessor(df, step, column)
    return preprocessorTransform(df, step)


def setPreprocessor(df, step, column):
    if(step is not None):
        step['preprocessor'] = preprocessor_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def preprocessorTransform(df, step):
    if(step is not None):
        step['preprocessor'].transform(df)
    return df


def preprocessorsInvert(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        for step in reversed(ps):
            df = preprocessorInvert(df, step)
    return df


def preprocessorInvert(df, step):
    if(step is not None):
        df = step['preprocessor'].invert_transform(df)
    return df


def clean_dataframe(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    dfConfig['keep_columns'] = dfConfig.get('keep_columns', True)
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    if (not dfConfig.get('keep_columns')):
        df = dataframe[specifiedColumnNames].copy()
    else:
        df = dataframe.copy()

    for c in specifiedColumn:
        df = preprocessorsAction(df, c)

    for c in specifiedColumn:
        df = encodersAction(df, c)

    return df


def invert_cleaning(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    df = dataframe.copy()

    for c in specifiedColumn:
        df = encodersInvert(df, c)

    for c in specifiedColumn:
        df = preprocessorsInvert(df, c)

    return df
