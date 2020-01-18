#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-sirtrevor',
    version='0.3.0',
    packages=['sirtrevor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app that provides a model field and ' +
                'corresponding widget based on the fantastic Sir Trevor ' +
                'project',
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/eGenGuru/django-sirtrevor',
    author='Eric Laugier (original author: Philipp Bosch)',
    author_email='eric.laugier@egen.guru',
    install_requires=['markdown2', 'django-appconf', 'django', 'six', 'Pillow-PIL', 'ez_setup', 'south'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
