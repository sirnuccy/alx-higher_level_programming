#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    from sys import argv

    count = len(sys.argv) - 1

    if count != 3:

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]

        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b))
        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b))
        else
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    
    else
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
