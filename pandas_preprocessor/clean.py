import pandas as pd
from pandas_preprocessor.utils import *
from pandas_preprocessor.preprocessors import *
from pandas_preprocessor.encoders import *


def get_dataframe(dataConfig):
    return pd.read_csv(dataConfig['connectionstring']) if dataConfig['format'] == 'csv' \
        else None


def setEncoders(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        foreach(lambda step: setEncoder(
            df, step, column), es)


def setEncoder(df, step, column):
    if(step is not None):
        step['encoder'] = encoder_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def encodersTransform(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        for step in es:
            df = encoderTransform(df, step)
    return df


def encoderTransform(df, step):
    if(step is not None):
        step['encoder'].transform(df)
    return df


def encodersInvert(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        for step in es:
            df = encoderInvert(df, step)
    return df


def encoderInvert(df, step):
    if(step is not None):
        step['encoder'].invert_transform(df)
    return df


def setPreprocessors(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        foreach(lambda step: setPreprocessor(
            df, step, column), ps)


def setPreprocessor(df, step, column):
    if(step is not None):
        step['preprocessor'] = preprocessor_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def preprocessorsTransform(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        for step in ps:
            df = preprocessorTransform(df, step)
    return df


def preprocessorTransform(df, step):
    if(step is not None):
        step['preprocessor'].transform(df)
    return df


def preprocessorsInvert(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        for step in ps:
            df = preprocessorInvert(df, step)
    return df


def preprocessorInvert(df, step):
    if(step is not None):
        df = step['preprocessor'].invert_transform(df)
    return df


def clean_dataframe(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    dfConfig['keeprows'] = dfConfig.get('keeprows', True)
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    if (not dfConfig.get('keeprows')):
        df = dataframe[specifiedColumnNames].copy()
    else:
        df = dataframe.copy()

    for c in specifiedColumn:
        setPreprocessors(df, c)

    for c in specifiedColumn:
        df = preprocessorsTransform(df, c)

    for c in specifiedColumn:
        setEncoders(df, c)

    for c in specifiedColumn:
        df = encodersTransform(df, c)

    return df


def invert_cleaning(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    if (not dfConfig.get('keeprows')):
        df = dataframe[specifiedColumnNames].copy()
    else:
        df = dataframe.copy()

    for c in specifiedColumn:
        df = encodersInvert(df, c)

    for c in specifiedColumn:
        df = preprocessorsInvert(df, c)

    return df
