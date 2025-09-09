from setuptools import setup, find_packages

setup(
    name='lister',
    version='0.1.0',
    description='A simple command line tool to list directory contents like ls',
    author='TA',
    author_email='ta472@exeter.ac.uk',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'lister = lister.cli:main',
        ],
    },
    python_requires='>=3.6',
)
