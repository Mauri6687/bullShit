'''
Created on 24.04.2019

@author: IMMaurC1
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Immaurc1",
    version="0.0.1",
    author="Calogero Maurici",
    author_email="calogero.maurici@med.uni-tuebingen.de",
    description="A restfull package for bwHC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mauri6687/bullShit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)