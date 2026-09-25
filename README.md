# pysfield

This repository is the Python migration of the `sfield` project. The package intentionally keeps the original runtime responsibilities and validation boundaries while delivering them through a Python package layout and executable tests.

## Layout

- `src/sfield/` — Python runtime package
- `tests/` — acceptance and regression coverage

## Smoke validation

```bash
python -m pytest -q
```
