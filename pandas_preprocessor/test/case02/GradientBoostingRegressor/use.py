import joblib
from pandas_preprocessor import *
import os
import toml

this_dir = os.path.dirname(os.path.realpath(__file__))
tomlLoc = os.path.join(this_dir, "config.toml")
config = toml.load(tomlLoc)
joblib_file = os.path.join(this_dir, config['model_file_location'])
# Load from file
model = joblib.load(joblib_file)

inputs = config['dataframe']['inputs']

for i in inputs:
    es = i.get('encoding_steps', [])
    for e in es:
        fl = nc(lambda: e['settings']['file_location'])
        if (fl is not None):
            e['settings']['file_location'] = os.path.join(this_dir, fl)

config['input_query']['connectionstring'] = os.path.join(
    this_dir, config['input_query']['connectionstring'])


df = get_dataframe(config['input_query'])
house_data = df.drop(['Address', 'Method', 'SellerG', 'Date',
                      'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)

house_data = clean_input(house_data, dfConfig=config['dataframe'])

print('Transformed DF')
print(house_data.head())

house_to_value = house_data.drop(['Price'], axis=1)

predicted_house_value = model.predict(house_to_value)

predicted_house_value = predicted_house_value[0]

# Print estimated value of the property to two decimal places

print("This property has an estimated value of AUD %.2f" %
      predicted_house_value)

inverted_house_data = invert_cleaning(house_data, config['dataframe'])

print('Inverted DF')
print(inverted_house_data.head())
