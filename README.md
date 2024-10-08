# ULN (Unique Learner Number) Package

This package provides utilities for working with Unique Learner Numbers (ULNs).

## Installation

You can install this package using pip:

```
pip install -e .
```

## Usage

```python
from uln import ULN, ULNValidator

# Create a ULN
uln = ULN.from_string("0000000042")

# Validate a ULN
is_valid = ULNValidator.is_valid_uln("0000000042")
```

## License

This project is licensed under the Apache License 2.0.