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

previous_output = None

while True:
    if previous_output is not None:
        print(f"\nPrevious output: {previous_output}")
    
    print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n" \
          "5. Use previous output\n" \
          "6. Exit\n")

    try:
        select = int(input("Select operations from 1, 2, 3, 4, 5, or 6: "))
        
        if select == 6:
            print("Exiting calculator. Goodbye!")
            break

        if select == 5:
            if previous_output is None:
                print("No previous output available. Please perform a calculation first.")
                continue
            else:
                while True:
                    try:
                        number_2 = float(input("Enter second number: "))
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                operation = int(input("Select operation from 1 (Add), 2 (Subtract), 3 (Multiply), or 4 (Divide): "))
                if operation == 1:
                    previous_output = add(previous_output, number_2)
                    print(previous_output)
                elif operation == 2:
                    previous_output = subtract(previous_output, number_2)
                    print(previous_output)
                elif operation == 3:
                    previous_output = multiply(previous_output, number_2)
                    print(previous_output)
                elif operation == 4:
                    previous_output = divide(previous_output, number_2)
                    print(previous_output)
                else:
                    print("Invalid input")

        else:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if select == 1:
                previous_output = add(number_1, number_2)
                print(previous_output)
            elif select == 2:
                previous_output = subtract(number_1, number_2)
                print(previous_output)
            elif select == 3:
                previous_output = multiply(number_1, number_2)
                print(previous_output)
            elif select == 4:
                previous_output = divide(number_1, number_2)
                print(previous_output)
            else:
                print("Invalid input")

    except ValueError:
        print("Invalid input. Please enter a number.")
