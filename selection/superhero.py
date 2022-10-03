import sys
from tkinter import *

root = Tk()
root.title("hello")
text_box = Text(root)

text_box.pack()

root.mainloop()

positives = ["y", "yes", "1", "true", "ye", "yea"]

if input("Is your superheros costume red?").lower() in positives:
    if input("Does your superhero own a weapons manufacturer?").lower() in positives:
        print("Your superhero is Iron man")
    else:
        print("Your superhero is Deadpool")
else:
    if input("Is your superhero primarily in a cartoon?").lower() not in positives:
        if input("Is your super heros identity hidden?").lower() in positives:
            print("Your superhero is batman, which is bad.", file=sys.stderr)
        else:
            print("Your superhero is superman, which is the most basic and bad option.", file=sys.stderr)
    else:
        if input("Does your superhero have 4 leg?").lower() not in positives:
            print("Your superhero is Shrek")
        else:
            print("Your super hero is donkey, which is the best choice")
            
