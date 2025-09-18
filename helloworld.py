import os

#Clear the terminal screen
os.system('cls')

#Make more visibly interesting
print("===SUPER COOL HELLO WORLD===")

#Good old hello
print("Hello World!!!")

print("Does the world say hello back?")
print("1. Yes")
print("2. No")
response = int(input("> "))

if response == 1:
    print("Hello to you too!!")
else:
    print("Oh... :(")