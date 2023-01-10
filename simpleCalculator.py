new_request = True

while new_request:
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("'+': addition, '-': substration, '*': multiplication, '/': division")

    request = input("What operation to do want to perform? ")

    if request == '+':
        print(num1 + num2)

    elif request == '-':
        print(num1 - num2)

    elif request == '*':
        print(num1 * num2)

    elif request == '/':
        print(num1/num2)

    else:
        print("Invalid operator")

    user_response = input("Do you want to perform another operation?(yes or no")
    if user_response == 'no':
        print("thank you for using this calculator")
        new_request = False


# Turn the program into a function