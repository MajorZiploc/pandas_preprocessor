To build project:

requires pipenv, python 3.8

In project root:

> pipenv shell
> pipenv install -e .
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['pandas_preprocessor', 'pandas_preprocessor.*']),

TODO:
Consider merging preprocessors and encoders into same flow and config. it may be useful to mix when these steps are done rather than preprocessor then encoder flow
Decide on whether some preprocessors should be skipped when processing the user query. Does it make sense to use missing value preprocessors on it? If so, they should be pickled from building the model. If not, then their should be a flag, or reuse the is_use_case flag to skip the transformation
Consider creating a config.toml scaffolding function. Given a dataframe, it creates a config.toml
Add sklearn.preprocessing.MultiLabelBinarizer
Add sklearn.preprocessing.KernelCenterer
Add sklearn.preprocessing.OrdinalEncoder
Validate that all sklearn class are using the correct and all params in constructors
Add error handling to selecting preprocessor and encoders with message of what the available transforms are
Adds means to add to the preprocessor and encoder dictionaries. It should not let the user add/reassign keys that already exist in the dictionary
Improve project documentation that shows on pypi and github page
Stacking encoders can lead to strange problems!!!! labelencoder has a problem when the indices dont come in order. example: if some are droped by mv_drop

Notes on Publishing
pipenv run python setup.py sdist bdist bdist_wheel
-- n is the end of the version being pushed
pipenv run twine upload dist/pandas_preprocessor-[version_number].tar.gz
