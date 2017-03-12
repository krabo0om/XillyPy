from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xillypy',
    version='0.1.0',
    packages=['xillypy'],
    url='https://github.com/krabo0om/XillyPy',
    license='MIT',
    author='Paul Genssler',
    author_email='p.genssler@freenet.de',
    description='A simple Xillybus interface written in Python',
    long_description=long_description,
    keywords='xillybus interface development',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Hardware',
        'Operating System :: Unix',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
