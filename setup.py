from setuptools import setup, find_packages

setup(
    name='Booklover09',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Devin McDonald',
    author_email='djm6cz@virginia.edu',
    description='Package containing files used in M09 HW',
    packages=find_packages(),    
    install_requires=['numpy', 'pandas'],
)
