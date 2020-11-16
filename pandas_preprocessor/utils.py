import os
import joblib


def foreach(action, iterable):
    for element in iterable:
        action(element)


def nc(supplier):
    try:
        return supplier()
    except AttributeError:
        return None


def set_full_paths(config, directory):
    config['model_file_location'] = os.path.join(
        directory, config['model_file_location'])
    if(not nc(lambda: config['input_query']['format']) == 'sql'):
        config['input_query']['connectionstring'] = os.path.join(
            directory, config['input_query']['connectionstring'])
    if(not nc(lambda: config['data']['format']) == 'sql'):
        config['data']['connectionstring'] = os.path.join(
            directory, config['data']['connectionstring'])
    inputs = config['dataframe']['inputs']
    for i in inputs:
        es = i.get('encoding_steps', [])
        for e in es:
            fl = nc(lambda: e['settings']['file_location'])
            if (fl is not None):
                e['settings']['file_location'] = os.path.join(directory, fl)


def load_model(config):
    model_file = config['model_file_location']
    model = joblib.load(model_file)
    return model

# df1 = r
# df2 = r.dropna(axis=0, how='any', thresh=None, subset=None)
# df3 = df1[~df1.isin(df2)].dropna(how='all')

# for (columnName, columnData) in cs.iteritems():
#     cs[columnName] = pd.to_numeric(
#         cs[columnName], downcast='integer')
