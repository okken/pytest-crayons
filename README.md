# pytest-crayons

A pytest plugin for colorful print statements.

## Installation

```
pip install pytest-crayons
```

## Usage

1. Include a color fixture in the param list of a test. 
2. Then use it instead of `print`.

```python
def test_magenta(magenta):
    blue("this should be magenta")
```

Just like normal print statements, you only see the output if:

* There's an failure in the test.
* or you pass in `-s` or `--capture=no`
* or you wrap the statement in a `with capsys.disabled():` block.

For our examples, we'll use `-s`:

![output of test_something](https://github.com/okken/pytest-crayons/blob/main/docs/magenta.png?raw=true)

## Available colors

* red 
* green
* yellow
* blue
* magenta
* cyan

Example with all colors: 

```python
def test_colors(red, green, yellow, blue, magenta, cyan):
    print("") # for the newline
    red("this should be red")
    green("this should be green")
    yellow("this should be yellow")
    blue("this should be blue")
    magenta("this should be magenta")
    cyan("this should be cyan")
```

![output of test_colors](https://github.com/okken/pytest-crayons/blob/main/docs/test_example.png?raw=true)

## This was included in a talk for PyCascades 2023

* Conference talk page : [Sharing is Caring - Sharing pytest Fixtures](https://2023.pycascades.com/program/talks/sharing-is-caring-sharing-pytest-fixtures/)
