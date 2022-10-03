def get_name():
    name = input("What is your name?")
    print(f"Welcome {name}")
    return name

get_name()

word = ""
while word.upper() not in ["0", "EXIT"]:
    word = input("Enter '0' or the word 'exit' to close")
    
print("Closing")
