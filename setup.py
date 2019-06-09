from setuptools import setup
setup(
    name="walrus-ast",
    entry_points = {
        'console_scripts': ["walrus-ast=vis:main"],
    }
)