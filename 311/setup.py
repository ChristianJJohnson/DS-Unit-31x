# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata-christianj",
    version="0.0.1",
    author="Christian Johnson",
    author_email="christian-johnson@lambdastudents.com",
    description="DSPT11 311 assignment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ChristianJJohnson/DS-Unit-31x/tree/master/311/lambdata_chrisjj",
    #keywords="",
    packages=find_packages() # ["lambdata_christianj"]
)