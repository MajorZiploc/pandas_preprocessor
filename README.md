To build project:

requires pipenv, python 3.8

In project root:

> pipenv shell
> pipenv install -e .
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['python01', 'python01.*']),

TODO:
Remove toml as a dependency
Remove test folder from export to dist
Add missing value preprocessors like mode and mean

Notes on Publishing
pipenv run python setup.py sdist bdist bdist_wheel
-- n is the end of the version being pushed
pipenv run twine upload dist/\*n.tar.gz
