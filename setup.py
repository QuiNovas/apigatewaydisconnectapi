import io

from setuptools import setup, find_packages

setup(
    name='apigatewaydisconnectapi',
    version='0.0.1',
    description='Provides a boto3 client class by the same name with a disconnect method for disconnecting websocket clients',
    author='Joseph Wortmann',
    author_email='jwortmann@quinovas.com',
    url='https://github.com/QuiNovas/apigatewaydisconnectapi',
    license='Apache 2.0',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    packages=['apigatewaydisconnectapi'],
    package_dir={'apigatewaydisconnectapi': 'src/apigatewaydisconnectapi'},
    package_data={'apigatewaydisconnectapi': ['models/apigatewaydisconnectapi/2018-11-29/*.json']},
    install_requires = [],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)
