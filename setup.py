from setuptools import setup

setup(
    name='fs-runway-finder',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'beautifulsoup4==4.9.1',
    ],
    py_modules=[
        'weather',
    ],
)
