"""
A file to install python library locally

Install by changing directory to /FreqResp/ then using $ pip install -e .

This installs with a symlink so changes to the source files will be immediately available to users of the package.

Installation is required for unit testing (pytest)
"""

from setuptools import setup

setup(
    name='FreqResp',
    version=0.0.0,
    description="""A package to quantify the frequency response of fishes using broadband sonar.  Or is it wideband? 
    Whatever they call it nowadays.""",
    url='https://github.com/kevinboswell/FreqResp',
    author='Papa Kevin Boswell',
    author_email='kevin.boswell@fiu.edu',
    license='MIT',
    packages=['FreqRespPy'],
    zip_safe=False)
