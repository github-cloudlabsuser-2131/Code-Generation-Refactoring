// This file serves as the entry point for the application.
// It imports the calculator functions from calculator.js and can include code to handle user input or command-line execution.

import { add, subtract, multiply, divide } from './calculator.js';

// Example usage
const a = 5;
const b = 3;

console.log(`Addition: ${a} + ${b} = ${add(a, b)}`);
console.log(`Subtraction: ${a} - ${b} = ${subtract(a, b)}`);
console.log(`Multiplication: ${a} * ${b} = ${multiply(a, b)}`);
console.log(`Division: ${a} / ${b} = ${divide(a, b)}`);