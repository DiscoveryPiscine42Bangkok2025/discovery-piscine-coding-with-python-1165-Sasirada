#!/usr/bin/env python3

user_input = input("Give me a number: ")

try :
    print(int(user_input))
except ValueError :
    user_float = float(user_input)
    print(user_float.__ceil__())