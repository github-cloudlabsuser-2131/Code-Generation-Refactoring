# Calculator Project

This is a simple calculator application that supports various mathematical operations including addition, subtraction, multiplication, and division. The project is designed to be user-friendly and allows for interactive input.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts one number from another.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides one number by another with error handling for division by zero.

## Project Structure

```
calculator-project
├── src
│   ├── calculator.py          # Main entry point for user interaction
│   ├── operations             # Contains operation modules
│   │   ├── addition.py        # Addition operation
│   │   ├── subtraction.py     # Subtraction operation
│   │   ├── multiplication.py   # Multiplication operation
│   │   ├── division.py        # Division operation
│   │   └── __init__.py       # Initializes operations module
│   └── utils                  # Contains utility functions
│       └── input_handler.py   # Handles user input
├── tests                      # Contains unit tests for operations
│   ├── test_addition.py       # Tests for addition
│   ├── test_subtraction.py    # Tests for subtraction
│   ├── test_multiplication.py  # Tests for multiplication
│   ├── test_division.py       # Tests for division
│   └── __init__.py           # Initializes tests module
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the calculator, execute the following command:

```
python src/calculator.py
```

Follow the prompts to perform calculations.

## Testing

To run the tests, use the following command:

```
pytest tests/
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.