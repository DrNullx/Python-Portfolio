# Simple Calculator

# Main functions used

def subtraction(x, y):
    return x - y


def addition(x, y):
    return x + y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# List of options
print('''\nWhat do you want to do?
1\tSubtraction
2\tAddition
3\tMultiply
4\tDivide 
''')

#main while loop
while True:
    choice = input("Please enter an option: ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
        if choice == '1':
            print('You chose to subtract', num1, 'and', num2)
            print('The answer is', subtraction(num1, num2))
    
        elif choice == '2':
            print('You chose to add', num1, 'and', num2)
            print('The answer is', addition(num1, num2))
    
        elif choice == '3':
            print('You chose to multiply', num1, 'and', num2)
            print('The answer is', multiply(num1, num2))
    
        elif choice == '4':
            print('You chose to divide', num1, 'and', num2)
            print('The answer is', divide(num1, num2))
        # asks the user if they want to do another calculation
        next_calculation = input(
            "Enter Y or N if you want to do another calculation:")
        next_calculation = next_calculation.upper()
        # Will stop the program if the user inputs N
        if next_calculation == 'N':
            break
    else:
        print("Invalid!")
