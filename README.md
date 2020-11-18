# To build project:

requires pipenv, python 3.8

In project root:

> pipenv shell  
> pipenv install -e .  
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements  
packages=find_packages(include=['pandas_preprocessor', 'pandas_preprocessor.*']),

# TODO:

- Consider merging preprocessors and encoders into same flow and config. it may be useful to mix when these steps are done rather than preprocessor then encoder flow
- Decide on whether some preprocessors should be skipped when processing the user query. Does it make sense to use missing value preprocessors on it? If so, they should be pickled from building the model. If not, then their should be a flag, or reuse the is_use_case flag to skip the transformation
- Consider creating a config.toml scaffolding function. Given a dataframe, it creates a config.toml
- Add sklearn.preprocessing.MultiLabelBinarizer
- Add sklearn.preprocessing.KernelCenterer
- Add sklearn.preprocessing.OrdinalEncoder
- Validate that all sklearn class are using the correct and all params in constructors
- Add error handling to selecting preprocessor and encoders with message of what the available transforms are
- Adds means to add to the preprocessor and encoder dictionaries. It should not let the user add/reassign keys that already exist in the dictionary
- Improve project documentation that shows on pypi and github page
- Stacking encoders can lead to strange problems!!!! labelencoder has a problem when the indices dont come in order. example: if some are droped by mv_drop

# Notes on Publishing

pipenv run python setup.py sdist bdist bdist_wheel  
-- n is the end of the version being pushed  
pipenv run twine upload dist/pandas_preprocessor-[version_number].tar.gz

# Benefits of using this library

- Allows for all preprocessing and encoding steps for each feature to be viewable in a simple config file.
- Gives you access to sklearn proprocessors and encoders without needed to know how to get them to work with your pandas dataframe. You can still use the same parameters that sklearn proprocessors and encoders accept.
- Allows for easy separation of the build process of a model and the use case of a model
- The same config will be able to process testing/training data as well as a real user query.
- Pickles (using joblib) your model, preprocessors (where applicable), and encoders after building the model. These pickles will be used during processing user queries
- Preprocessors and encoders support transform, most support inverse_transform. This allows for you to transform a dataframe and then transform it back to the original. Some inversions are not supported though

# Example use cases

Look at pandas_preprocessor/test folder for example use cases

- case01: purely an example of applying preprocessors and encoders to a dataframe and applying inverse transforms to the dataframe
- case02: builds/trains the model in build.py and uses the model for a user query in use.py. The preprocessing steps and encoding steps are very simple here.
