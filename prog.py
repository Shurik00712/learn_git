from random import randint
a = input()
b = input()
print(f"You entered characters: {a} {b}. Random operation: {eval(a+['-', '+', '*', '**', '%'][randint(0, 4)]+b)}")
