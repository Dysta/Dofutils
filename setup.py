from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dofutils',
    version='0.0.2',
    packages=find_packages(exclude="tests"),
    url='https://github.com/Dysta/Dofutils',
    license='',
    author='Dysta',
    author_email='',
    description='Collection of useful things for build Dofus Retro bot/emulator ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
)
