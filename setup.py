from distutils.core import setup
from sys import version

if version.split('.')[0] < '3':
    raise RuntimeError("Only Python 3 is supported.")

setup(
    name='names',
    version='1.0',
    packages=['names'],
    package_data={'names': ['data/*.csv']},
    url='https://github.com/gunziptarball/names',
    license='MIT',
    author='Action Jaxon Flaxon-Waxon',
    author_email='jackson.j.gilman@gmail.com',
    description='A really, really, really stupid name generator',
    entry_points={
        'console_scripts': [
            'names = names.main:main_from_cli'
        ]
    }
)
