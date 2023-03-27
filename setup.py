from os import path
from codecs import open
from setuptools import setup

package_name = "punycode"

root_dir = path.abspath(path.dirname(__file__))

def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt'), encoding="utf-8-sig").readlines()]

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    description='Punycode Converter Library for Python',
    version='0.2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Yutsuro/punycode',
    author='Yutsuro',
    author_email='Yuki@utsu.ro',
    license='MIT',
    keywords='Punycode Converter Python',
    packages=[package_name],
    install_requires=_requirements(),
    classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Internet :: Name Service (DNS)',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)