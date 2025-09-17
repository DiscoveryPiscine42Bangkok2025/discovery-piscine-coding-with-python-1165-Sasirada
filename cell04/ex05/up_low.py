#!/usr/bin/env python3

user_input = input()
new_str = ""

for i in user_input :
    if (i.isupper()) :
        new_str += i.lower()
    else :
        new_str += i.upper()
print(new_str)