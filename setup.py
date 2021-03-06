#!/usr/bin/env python

from setuptools import find_packages, setup


VERSION = '1.2.0'
REPO_URL = 'https://github.com/drongo-framework/drongo-wing-media'
DOWNLOAD_URL = REPO_URL + '/archive/v{version}.tar.gz'.format(version=VERSION)

setup(
    name='drongo-wing-media',
    version=VERSION,
    description='Drongo wing session module.',
    author='Sattvik Chakravarthy, Sagar Chakravarthy',
    author_email='sattvik@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=find_packages(),
    install_requires=[
        'drongo>=1.2.0',
        'drongo-wing-module>=1.2.0',
    ],
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    include_package_data=True,
    zip_safe=False,
)
