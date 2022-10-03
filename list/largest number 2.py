from time import sleep
from random import choice
from os import system

global chars
chars = list("1234567890")

def rand():
    return "".join([choice(chars) for x in range(20)])

for x in range(30):
    print(rand())
    sleep(0.01)
    system("cls")

print(max([32, 90, 321]))

input()
