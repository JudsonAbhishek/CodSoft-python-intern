
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

while True:
    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n" \
            "5. Exit\n")

  
    try:
        select = int(input("Select operations from 1, 2, 3, 4, or 5: "))
        if select == 5:
            print("Exiting calculator. Goodbye!")
            break

        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if select == 1:
            print(number_1, "+", number_2, "=", add(number_1, number_2))
        elif select == 2:
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))
        elif select == 3:
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))
        elif select == 4:
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
        else:
            print("Invalid input")

    except ValueError:
        print("Invalid input. Please enter a number.")
