#!/usr/bin/env python3

user_input = input("Give me a number: ")

try :
    user_int = int(user_input)
    print("This number is an integer.")
except ValueError :
    try :
        user_float = float(user_input)
        if (user_float.is_integer()) :
            print("This number is an integer.")
        else :
            print("This number is a decimal.")
    except ValueError :
        print("Not a number.")