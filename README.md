# GF 256 Operations

This is a Python project that implements operations in the Galois Field GF(2^8) in python.
## Getting Started
### Dependencies
- Python 3.x


### Installing
Clone the repository using the following command:

```bash
git clone https://github.com/01-00-11-00/gf_256_operations.git
```

## Function Overview
This project contains a class `GF256Operations` with the following methods:

- `__init__(self, minimal_polynomial: int)`: This is the constructor of the class. It initializes the instance with a minimal polynomial.

- `get_degree(a) -> int`: This static method returns the degree of a given polynomial `a`.

- `add(a: int, b: int) -> int`: This static method performs the addition of two numbers `a` and `b` in GF(2^8) and returns the result.

- `multiply(self, a: int, b:int) -> int`: This method multiplies two numbers `a` and `b` in GF(2^8) and returns the result.

- `modular_reduction(self, a: int) -> int`: This method performs a modular reduction of a number `a` in GF(2^8) and returns the result.

- `invert(self, a) -> int`: This method inverts a number `a` in GF(2^8) and returns the inverse of the number.

Each of these methods is designed to perform a specific operation in the Galois Field GF(2^8).

## Authors
01-00-11-00

ex. [@01-00-11-00](https://github.com/01-00-11-00)

## Version History
- 0.1
    - Initial Release