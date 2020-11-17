import pandas as pd
from pandas_preprocessor.utils import *
from pandas_preprocessor.preprocessors import *
from pandas_preprocessor.encoders import *


class DFCleaningHelper(object):

    def __init__(self, is_use_case):
        self.is_use_case = is_use_case

    def encodersAction(self, df, column):
        es = column.get('encoding_steps')
        if(es is not None):
            for step in es:
                df = self.encoderAction(df, step, column)
        return df

    def encoderAction(self, df, step, column):
        self.setEncoder(df, step, column)
        return self.encoderTransform(df, step)

    def setEncoder(self, df, step, column):
        if(step is not None):
            settings = step.get('settings', {})
            settings['is_use_case'] = self.is_use_case
            step['encoder'] = encoder_selector(
                step['algo'])(column['name'], df, step.get('settings'))

    def encoderTransform(self, df, step):
        if(step is not None):
            df = step['encoder'].transform(df)
        return df

    def encodersInvert(self, df, column):
        es = column.get('encoding_steps')
        if(es is not None):
            for step in reversed(es):
                df = self.encoderInvert(df, step)
        return df

    def encoderInvert(self, df, step):
        if(step is not None):
            df = step['encoder'].invert_transform(df)
        return df

    def preprocessorsAction(self, df, column):
        ps = column.get('preprocess_steps')
        if(ps is not None):
            for step in ps:
                df = self.preprocessorAction(df, step, column)
        return df

    def preprocessorAction(self, df, step, column):
        self.setPreprocessor(df, step, column)
        return self.preprocessorTransform(df, step)

    def setPreprocessor(self, df, step, column):
        if(step is not None):
            settings = step.get('settings', {})
            settings['is_use_case'] = self.is_use_case
            step['preprocessor'] = preprocessor_selector(
                step['algo'])(column['name'], df, step.get('settings'))

    def preprocessorTransform(self, df, step):
        if(step is not None):
            step['preprocessor'].transform(df)
        return df

    def preprocessorsInvert(self, df, column):
        ps = column.get('preprocess_steps')
        if(ps is not None):
            for step in reversed(ps):
                df = self.preprocessorInvert(df, step)
        return df

    def preprocessorInvert(self, df, step):
        if(step is not None):
            df = step['preprocessor'].invert_transform(df)
        return df


def get_dataframe(dataConfig):
    return pd.read_csv(dataConfig['connectionstring']) if dataConfig['format'] == 'csv' \
        else None


def invert_cleaning_query(dataframe, dfConfig):
    dfCleaningHelper = DFCleaningHelper(is_use_case=False)
    return invert_cleaning(dataframe, dfConfig, dfCleaningHelper)


def clean_query(dataframe, dfConfig):
    dfCleaningHelper = DFCleaningHelper(is_use_case=True)
    return clean_dataframe(dataframe, dfConfig, dfCleaningHelper)


def clean_dataframe(dataframe, dfConfig, dfCleaningHelper=DFCleaningHelper(is_use_case=False)):
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
        df = dfCleaningHelper.preprocessorsAction(df, c)

    for c in specifiedColumn:
        df = dfCleaningHelper.encodersAction(df, c)

    return df


def invert_cleaning(dataframe, dfConfig, dfCleaningHelper=DFCleaningHelper(is_use_case=False)):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    specifiedColumn = inputs + outputs

    specifiedColumnNames = [i['name'] for i in specifiedColumn]

    df = dataframe.copy()

    for c in specifiedColumn:
        df = dfCleaningHelper.encodersInvert(df, c)

    for c in specifiedColumn:
        df = dfCleaningHelper.preprocessorsInvert(df, c)

    return df
