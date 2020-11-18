import os
import joblib


def foreach(action, iterable):
    for element in iterable:
        action(element)


def nc(supplier):
    try:
        return supplier()
    except (AttributeError, KeyError, TypeError):
        return None


def set_full_paths(config, directory):
    config['model_file_location'] = os.path.join(
        directory, config['model_file_location'])
    inq_format = nc(lambda: config.get('input_query').get('format'))
    if(inq_format is not None and not inq_format == 'sql'):
        config['input_query']['connectionstring'] = os.path.join(
            directory, config['input_query']['connectionstring'])
    d_format = nc(lambda: config.get('data').get('format'))
    if(d_format is not None and not d_format == 'sql'):
        config['data']['connectionstring'] = os.path.join(
            directory, config['data']['connectionstring'])

    inputs = config['dataframe']['inputs']
    outputs = config['dataframe']['outputs']

    def file_location_updater(lst, steps):
        for l in lst:
            ss = l.get(steps, [])
            for s in ss:
                fl = nc(lambda: s.get('settings').get('file_location'))
                if (fl is not None):
                    s['settings']['file_location'] = os.path.join(
                        directory, fl)
    file_location_updater(inputs, 'preprocess_steps')
    file_location_updater(inputs, 'encoding_steps')
    file_location_updater(outputs, 'preprocess_steps')
    file_location_updater(outputs, 'encoding_steps')


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
