from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dofutils',
    version='0.0.3',
    packages=find_packages(exclude=["tests", "tests.*"]),
    url='https://github.com/Dysta/Dofutils',
    license='',
    author='Dysta',
    description='Collection of useful things for build Dofus Retro bot/emulator ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='dofus, dofus retro, retro, bot, emulateur', 
    python_requires='>=3.8',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha'
    ]
)
