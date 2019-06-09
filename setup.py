from setuptools import setup
from setuptools import find_packages

setup(
    name="walrus-ast",
    packages=find_packages("."),
    entry_points={
        'console_scripts': [
            "walrus-ast=pre_commit_hooks.walrus_ast:main",
            "walrus-opportunity=pre_commit_hooks.walrus_opportunity:main"
        ],
    },
    install_requires=[
        "astpath[xpath]"
    ],
)
