from setuptools import setup

setup(
    name="hooks",
    py_modules=["walrus_ast", "walrus_opportunity"],
    entry_points={
        'console_scripts': [
            "walrus-ast=walrus_ast:main",
            "walrus-opportunity=walrus_opportunity:main"
        ],
    },
    install_requires=[
        # Dep. for `walrus-opportunity`
        "astpath[xpath]",
    ],
)
