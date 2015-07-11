#!/usr/bin/env python
from distutils.core import setup
from os.path import isfile, isdir
from os import listdir

setup(
    name='metaengine',
    version='1.0',
    description='Meta Engine Utilities',
    author='Jaden Wu',
    author_email='wslgb2006@gmail.com',
    url='http://jadesoul.sinaapp.com/',
    license='Python Software Foundation License',
    #packages=['libjade', 'libjade/database'],
    scripts=filter(isfile, ['scripts/'+i for i in listdir('scripts')]),
)

