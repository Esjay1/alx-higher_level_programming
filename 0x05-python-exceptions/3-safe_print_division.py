#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        test = a / b
    except Exception as e:
        test = None
    finally:
        print("Inside result: {}".format(test))
        return (test)
