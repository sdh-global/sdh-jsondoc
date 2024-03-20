#!/usr/bin/env python
from setuptools import find_packages, setup

version = '0.3.4'

setup(
    name='sdh.jsondoc',
    version=version,
    url='https://bitbucket.org/sdh-llc/sdh.jsondoc',
    author='Software Development Hub LLC',
    author_email='dev-tools@sdh.com.ua',
    description='Utils to store data into json',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['sdh'],
    eager_resources=['sdh'],
    include_package_data=True,
    entry_points={},
    install_requires=['Django>=2.2', ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
