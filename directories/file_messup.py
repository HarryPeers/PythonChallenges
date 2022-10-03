from random import choice, randint
import os

global chars
chars = list("abcdefghijklmnopqurstvwxyz")

def rand_name():
    return "".join([choice(chars) for x in range(10)])

directory = f"{os.getcwd()}/messup"

for ext in [".py", ".pyc", ".txt", ".css", ".html", ".css"]:
    break
    for x in range(20):
        with open(f"{directory}/dump/{rand_name()}{ext}", "w") as file:
            pass

for file in os.listdir(f"{directory}/dump/"):
    name, ext = file.split(".")
    
