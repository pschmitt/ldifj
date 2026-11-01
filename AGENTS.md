# Agent notes

`ldifj` is a Python command-line parser that converts LDIF input to JSON.

- Preserve the command-line interface and streaming behavior documented in
  `README.md`.
- The CI lint workflow uses the shared
  [ci-workflows](https://github.com/pschmitt/ci-workflows) Python lint action.
- Run `python -m compileall -q ldifj.py` for a local syntax check.
- Before changing CI, check for a reusable workflow or action there and
  preserve the caller's existing behavior and check coverage.
- There is no dedicated test suite. Use representative LDIF fixtures when
  checking parser changes and avoid including real directory data in fixtures.
- PyPI and GitHub release workflows run on version tags; ordinary development
  changes must not create tags.
