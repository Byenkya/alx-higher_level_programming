#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisonError:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result
