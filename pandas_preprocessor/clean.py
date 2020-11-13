import numpy as np
import pandas as pd
import toml
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
        foreach(lambda step: encoderTransform(
            df, step), es)


def encoderTransform(df, step):
    if(step is not None):
        step['encoder'].transform(df)


def encodersInvert(df, column):
    es = column.get('encoding_steps')
    if(es is not None):
        foreach(lambda step: encoderInvert(
            df, step), es)


def encoderInvert(df, step):
    if(step is not None):
        step['encoder'].invert_transform(df)


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
        foreach(lambda step: preprocessorTransform(
            df, step), ps)


def preprocessorTransform(df, step):
    if(step is not None):
        step['preprocessor'].transform(df)


def preprocessorsInvert(df, column):
    ps = column.get('preprocess_steps')
    if(ps is not None):
        foreach(lambda step: preprocessorInvert(
            df, step), ps)


def preprocessorInvert(df, step):
    if(step is not None):
        step['preprocessor'].invert_transform(df)


def clean_dataframe(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    allColumns = inputs + outputs

    requiredColumns = [i['name'] for i in allColumns]

    df = dataframe[requiredColumns].copy()

    for c in allColumns:
        setPreprocessors(df, c)

    for c in allColumns:
        preprocessorsTransform(df, c)

    for c in allColumns:
        setEncoders(df, c)

    for c in allColumns:
        encodersTransform(df, c)

    return df


def invert_cleaning(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    allColumns = inputs + outputs

    requiredColumns = [i['name'] for i in allColumns]

    df = dataframe[requiredColumns].copy()

    for c in allColumns:
        encodersInvert(df, c)

    for c in allColumns:
        preprocessorsInvert(df, c)

    return df
