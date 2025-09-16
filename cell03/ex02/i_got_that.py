#!/usr/bin/env python3

user_input = input("What you gotta say? : ")
stop = "STOP"
if (user_input != stop) :
    cont = True
    while (cont) :
        new_input = input("I got that! Anything else? : ")
        if (new_input == stop) :
            cont = False