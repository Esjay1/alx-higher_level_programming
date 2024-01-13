#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)
    if len(sys.argv) == 4:
        if sys.argv[2] == '+':
            print("{} + {} = \
{}".format(a, b, calculator_1.add(a, b)), end="\n")
        if sys.argv[2] == '-':
            print("{} - {} = \
{}".format(a, b, calculator_1.sub(a, b)), end="\n")
        if sys.argv[2] == '*':
            print("{} * {} = \
{}".format(a, b, calculator_1.mul(a, b)), end="\n")
        if sys.argv[2] == '/':
            print("{} / {} = \
{}".format(a, b, calculator_1.div(a, b)), end="\n")
        if sys.argv[2] not in ['+', '-', '*', '/']:
            print("Unknown operator. Available \
operators: +, -, * and /", end="\n")
            sys.exit(1)
