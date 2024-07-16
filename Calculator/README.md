# Calculator Application

This is a simple calculator application implemented in Python. The application supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

1. **Addition**: Adds two numbers.
2. **Subtraction**: Subtracts the second number from the first number.
3. **Multiplication**: Multiplies two numbers.
4. **Division**: Divides the first number by the second number.

## Implementation Details

### Functions

1. **add(n1, n2)**: This function takes two numbers as input and returns their sum.
2. **subtract(n1, n2)**: This function takes two numbers as input and returns the difference (n1 - n2).
3. **multiply(n1, n2)**: This function takes two numbers as input and returns their product.
4. **divide(n1, n2)**: This function takes two numbers as input and returns the quotient (n1 / n2).

### Operations Dictionary

The `operations` dictionary maps operation symbols to their corresponding functions:
```
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
```

### Main Function: calculator()

1. **Display Logo**: The application starts by displaying a logo (imported from an external file `Art`).
2. **First Number Input**: Prompts the user to input the first number.
3. **Operations Display**: Displays the available operations (`+`, `-`, `*`, `/`).
4. **While Loop**: The main calculation loop allows the user to perform multiple operations sequentially without restarting the application.
   - **Operation Symbol Input**: Prompts the user to select an operation.
   - **Second Number Input**: Prompts the user to input the next number.
   - **Calculation**: Performs the calculation based on the selected operation and displays the result.
   - **Continuation Check**: Asks the user if they want to continue calculating with the current result or start a new calculation. If the user chooses to continue, the current result becomes the new first number for the next operation.

### Clear Function

The `clear` function is imported from the `replit` module and is used to clear the console for a fresh start when the user decides to start a new calculation.

## Usage

To use this calculator, simply run the script. The program will prompt you for inputs and display results based on your selected operations. You can continue calculations with the current result or start a new calculation anytime.

---
