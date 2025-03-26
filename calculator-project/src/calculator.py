def main():
    print("Welcome to the Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                from operations.addition import add
                result = add(num1, num2)
                print(f"The result of addition is: {result}")

            elif choice == '2':
                from operations.subtraction import subtract
                result = subtract(num1, num2)
                print(f"The result of subtraction is: {result}")

            elif choice == '3':
                from operations.multiplication import multiply
                result = multiply(num1, num2)
                print(f"The result of multiplication is: {result}")

            elif choice == '4':
                from operations.division import divide
                result = divide(num1, num2)
                print(f"The result of division is: {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()