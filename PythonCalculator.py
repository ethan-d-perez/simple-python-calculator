blocker = "------------------------------------------------------------------------------------------------------------"
start_msg = "Welcome to the Python Calcluator."
operation_txt = """What operation do you want to perform? Type "cancel" to close the calculator.
"""
first_num_txt = """What is the first number?
"""
second_num_txt = """What is the second number?
"""
first_num = 0.0
second_num = 0.0
operation = ""

print(blocker)
print(start_msg)

def calculator_logic():
    print(blocker)

    global operation
    operation = input(operation_txt)
    if operation == "add" or operation == "addition" or operation == "plus":
        operation = "add"
        first_number()
    if operation == "sub" or operation == "subtraction" or operation == "subtract" or operation == "minus":
        operation = "subtract"
        first_number()
    if operation == "times" or operation == "multiply" or operation == "multiplication":
        operation = "multiply"
        first_number()
    if operation == "divide" or operation == "division":
        operation = "divide"
        first_number()
    if operation == "quit" or operation == "cancel":
        print("Goodbye!")
        quit()
    else:
        print("I do not understand that operation. You might've typed it incorrectly. Try typing 'add', 'sub', 'multiply', or 'divide' in the input space.")
        calculator_logic()

def first_number():
    try:
        global first_num
        first_number = float(input(first_num_txt))
        first_num = first_number
    except ValueError:
        print("Please use only numbers and decimal points.")
        first_number()
    else:
        second_number()

def second_number():
    try:
        global second_num
        second_number = float(input(second_num_txt))
        second_num = second_number
    except ValueError:
        print("Please use only numbers and decimal points.")
        second_number()
    else:
        global operation
        match operation:
            case "add":
                adding()
            case "subtract":
                subtracting()
            case "multiply":
                multiplying()
            case "divide":
                dividing()
            case _:
                print("I never got an operation type, let's start from the beginning.")
                calculator_logic()

def adding():
    global first_num
    global second_num
    ans = first_num + second_num
    print("Your sum is: ")
    print(ans)
    calculator_logic()

def subtracting():
    global first_num
    global second_num
    ans = first_num - second_num
    print("Your difference is: ")
    print(ans)
    calculator_logic()

def multiplying():
    global first_num
    global second_num
    ans = first_num * second_num
    print("Your product is: ")
    print(ans)
    calculator_logic()

def dividing():
    global first_num
    global second_num
    ans = first_num / second_num
    print("Your quotient is: ")
    print(ans)
    calculator_logic()

calculator_logic()