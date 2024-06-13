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
                print(f"Your previous output is: {previous_output}")
                number_1 = previous_output
                number_2 = float(input("Enter second number: "))
        else:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

        if select == 1:
            previous_output = add(number_1, number_2)
            print(number_1, "+", number_2, "=", previous_output)
        elif select == 2:
            previous_output = subtract(number_1, number_2)
            print(number_1, "-", number_2, "=", previous_output)
        elif select == 3:
            previous_output = multiply(number_1, number_2)
            print(number_1, "*", number_2, "=", previous_output)
        elif select == 4:
            previous_output = divide(number_1, number_2)
            print(number_1, "/", number_2, "=", previous_output)
        elif select == 5:
            print(f"Using previous output ({previous_output}) as the first number.")
        else:
            print("Invalid input")
        
        print()  

    except ValueError:
        print("Invalid input. Please enter a number.")
        print()  