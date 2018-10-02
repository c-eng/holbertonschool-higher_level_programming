#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as errar:
        print("Exception: {}".format(errar), file=sys.stderr)
        return False
    return True
