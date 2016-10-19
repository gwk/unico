# Dedicated to the public domain under CC0: https://creativecommons.org/publicdomain/zero/1.0/.

# distutils setup script.
# users should install with: `$ pip3 install unico`
# developers can make a local install with: `$ pip3 install -e .`
# upload to pypi test server with: `$ python3 setup.py sdist upload -r pypitest`
# upload to pypi prod server with: `$ python3 setup.py sdist upload`

from setuptools import setup

long_description = '''
Unico provides Unicode metadata parsed directly from the published standard data.
It was created to facilitate correct lexing/parsing of Unicode text.
The project is hosted at 'https://github.com/gwk/unico'.
'''

setup(
  name='unico',
  license='CC0',
  version='0.0.0',
  author='George King',
  author_email='george.w.king@gmail.com',
  url='https://github.com/gwk/unico',
  description='Unico provides Unicode metadata parsed directly from the published standard data.',
  long_description=long_description,
  packages=['unico'],
  keywords=['Unicode', 'lexer', 'parser', 'parsing', 'tokenizer'],
  classifiers=[ # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development',
  ],
)
