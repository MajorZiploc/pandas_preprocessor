import pandas as pd
from pandas_preprocessor.utils import *
from pandas_preprocessor.processors import *
from pandas_preprocessor.processors.encoders import *


def get_dataframe(dataConfig):
    return pd.read_csv(dataConfig['connectionstring']) if dataConfig['format'] == 'csv' \
        else None


def encodersAction(df, column, is_use_case):
    es = column.get('encoding_steps')
    if(es is not None):
        for step in es:
            df = encoderAction(df, step, column, is_use_case)
    return df


def encoderAction(df, step, column, is_use_case):
    setEncoder(df, step, column, is_use_case)
    return encoderTransform(df, step)


def setEncoder(df, step, column, is_use_case):
    if(step is not None):
        settings = step.get('settings', {})
        settings['is_use_case'] = is_use_case
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


def processorsAction(df, column, is_use_case):
    ps = column.get('process_steps')
    if(ps is not None):
        for step in ps:
            df = processorAction(df, step, column, is_use_case)
    return df


def processorAction(df, step, column, is_use_case):
    setProcessor(df, step, column, is_use_case)
    return processorTransform(df, step)


def setProcessor(df, step, column, is_use_case):
    if(step is not None):
        settings = step.get('settings', {})
        settings['is_use_case'] = is_use_case
        step['processor'] = processor_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def processorTransform(df, step):
    if(step is not None):
        step['processor'].transform(df)
    return df


def processorsInvert(df, column):
    ps = column.get('process_steps')
    if(ps is not None):
        for step in reversed(ps):
            df = processorInvert(df, step)
    return df


def processorInvert(df, step):
    if(step is not None):
        df = step['processor'].invert_transform(df)
    return df


def clean_input(dataframe, dfConfig):
    return clean_dataframe(dataframe, dfConfig, is_use_case=True)


def clean_dataframe(dataframe, dfConfig, is_use_case=False):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    dfConfig['keep_other_columns'] = dfConfig.get('keep_other_columns', True)
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    if (not dfConfig.get('keep_other_columns')):
        df = dataframe[specifiedColumnNames].copy()
    else:
        df = dataframe.copy()

    for c in specifiedColumn:
        df = processorsAction(df, c, is_use_case)

    for c in specifiedColumn:
        df = encodersAction(df, c, is_use_case)

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
        df = processorsInvert(df, c)

    return df
