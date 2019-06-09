# pre-commit-hooks

## Trying out (from user perspective)

- `git init` (from any empty folder)
- copy `pre-commit-hooks/.pre-commit-config.yaml` into
- experiment adding files from `input` folder to git staged and running trying to make commit

## Developing new hooks

- `git init` (from any empty folder next to cloned `pre-commit-hooks`)
- run
```
$ pre-commit try-repo ../pre-commit-hooks walrus-grep --verbose --all-files
```

## TODO
- handle different `language_version`s of python, e.g. 3.7 and 3.8 (different `setup.py`s?)
