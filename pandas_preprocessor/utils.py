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
    config['model_file_location'] = os.path.join(directory, config['model_file_location'])
    config['input_query']['connectionstring'] = os.path.join(
        directory, config['input_query']['connectionstring'])
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
