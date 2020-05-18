# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata-ChrisJJ",
    version="1.0",
    author="Christian Johnson",
    author_email="christianjerelj@icloud.com",
    description="DSPT4 311 assignment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ChristianJJohnson/DS-Unit-3/tree/master/Sprint%201/Module%201/311a",
    #keywords="",
    packages=find_packages() # ["lambdata_chrisjj"]
)