try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print('''what kind of operation do you want to perform.\n Press + for addition \n Press - for subtraction \n Press * for multiplication \n Press / for division''')

    o = input("Enter the operation you want to perform: ")    

    match o:
        case "+":
            print(f"The sum of {a} and {b} is {a+b}")
        case "-":
            print(f"The difference of {a} and {b} is {a-b}")
        case "*":
            print(f"The product of {a} and {b} is {a*b}")
        case "/":
            if b != 0:
                print(f"The quotient of {a} and {b} is {a/b}")
            else:
                print("Cannot divide by zero")
        case _:
            print("Invalid operation") 

except Exception as e:
    print("Enter a valid value of a and b")

