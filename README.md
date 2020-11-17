To build project:

requires pipenv, python 3.8

In project root:

> pipenv shell
> pipenv install -e .
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['pandas_preprocessor', 'pandas_preprocessor.*']),

TODO:
Remove toml as a dependency
Remove test folder from export to dist
Add pickling to label and one hot encoders / one hot encoder will have to use sklearns version
Consider merging preprocessors and encoders into same flow and config. it may be useful to mix when these steps are done rather than preprocessor then encoder flow
Add settings params for each encoder and preprocessing based on sklearn docs
Decide on whether some preprocessors should be skipped when processing the user query. Does it make sense to use missing value preprocessors on it? If so, they should be pickled from building the model. If not, then their should be a flag, or reuse the is_use_case flag to skip the transformation

Notes on Publishing
pipenv run python setup.py sdist bdist bdist_wheel
-- n is the end of the version being pushed
pipenv run twine upload dist/pandas_preprocessor-[version_number].tar.gz
