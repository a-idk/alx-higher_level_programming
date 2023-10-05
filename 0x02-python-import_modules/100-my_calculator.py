#!/usr/bin/python3
# @a_idk scripting

# program that imports all functions from the file calculator_1.py
# and handles basic operations.

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div 

    # If the number of arguments is not 3
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # If the operator is not the +-*/
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # assigning variables a and b
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # printing the result
    print(f"{a} {sys.argv[2]} {b} = {operators[sys.argv[2]](a, b)}")
