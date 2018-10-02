#!/usr/bin/python3
def safe_function(fct, *args):
    try:
       result = fct(*args)
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as err:
        print("{}".format(err), file=stderr)
        return None
    return result
