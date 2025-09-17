#!/usr/bin/env python3

user_input = int(input("Please tell me your age: "))
print(f"You are currently {user_input} years old.")
years = 10
while (years <= 30) :
    print(f"In {years} years, you'll be {user_input + years} years old.")
    years += 10