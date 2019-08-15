from os import environ, pathsep
from os.path import abspath, dirname, join

models_path = join(abspath(dirname(__file__)), 'models')
environ['AWS_DATA_PATH'] = environ['AWS_DATA_PATH'] + pathsep + models_path if environ.get('AWS_DATA_PATH') else models_path
