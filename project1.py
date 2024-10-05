def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot compute modulus with divisor zero.")
    return x % y


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            try:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result:.2f}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            try:
                result = modulus(num1, num2)
                print(f"{num1} % {num2} = {result}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid choice. Please select a number between 1 to 5.")


main()

