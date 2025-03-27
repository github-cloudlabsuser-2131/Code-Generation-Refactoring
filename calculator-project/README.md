# Calculator Project

This is a simple calculator project implemented in JavaScript. It provides basic arithmetic operations including addition, subtraction, multiplication, and division.

## Project Structure

```
calculator-project
├── src
│   ├── calculator.js
│   └── index.js
├── package.json
└── README.md
```

## Installation

To run this project, you need to have Node.js installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the dependencies by running the following command:

   ```
   npm install
   ```

4. Run the calculator by executing the following command:

   ```
   node src/index.js
   ```

## Functions

The calculator supports the following operations:

- **Addition**: `add(a, b)`
- **Subtraction**: `subtract(a, b)`
- **Multiplication**: `multiply(a, b)`
- **Division**: `divide(a, b)`

## Examples

```javascript
// Example usage
const { add, subtract, multiply, divide } = require('./calculator');

const result1 = add(5, 3);        // Returns 8
const result2 = subtract(10, 4);  // Returns 6
const result3 = multiply(2, 3);   // Returns 6
const result4 = divide(8, 2);     // Returns 4
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.