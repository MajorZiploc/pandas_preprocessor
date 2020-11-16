import pandas as pd
import toml
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import math
import joblib
from pandas_preprocessor import *
import os


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, l(df))


this_dir = os.path.dirname(os.path.realpath(__file__))
tomlLoc = os.path.join(this_dir, "config.toml")
# print(tomlLoc)
config = toml.load(tomlLoc)
fileLoc = os.path.join(this_dir, config['data']['connectionstring'])
# print(fileLoc)
config['data']['connectionstring'] = fileLoc

inputs = config['dataframe']['inputs']

for i in inputs:
    es = i.get('encoding_steps', [])
    for e in es:
        fl = nc(lambda: e['settings']['file_location'])
        if (fl is not None):
            e['settings']['file_location'] = os.path.join(this_dir, fl)

df = get_dataframe(config['data'])


r = df.drop(['Address', 'Method', 'SellerG', 'Date',
             'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)
# p(r)
print(r.shape)
r.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

print(r.shape)
# p(r)

r = clean_dataframe(r, config['dataframe'])

# print(r.head())
print('Cleaned DF')
p(r)
inverted_df = invert_cleaning(r, config['dataframe'])
print('Inverted DF')
p(inverted_df)

# X = r.drop('Price', axis=1)
# y = r['Price']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, shuffle=True)

# h = r.head()

# l = [h, len(df), len(r)]

# foreach(print, l)

# model = ensemble.GradientBoostingRegressor(
#     n_estimators=250,
#     learning_rate=0.1,
#     max_depth=5,
#     min_samples_split=4,
#     min_samples_leaf=6,
#     max_features=0.6,
#     loss='huber'
# )

# model.fit(X_train, y_train)

# mae_train = mean_absolute_error(y_train, model.predict(X_train))

# print("Training Set Mean Absolute Error: %.2f" % mae_train)

# mae_test = mean_absolute_error(y_test, model.predict(X_test))
# print("Test Set Mean Absolute Error: %.2f" % mae_test)

# joblib_file = "house_model.pkl"
# joblib.dump(model, joblib_file)
