def double_letters(sentence:str):
    previous = None
    double = False
    for char in sentence:
        if char.lower() == previous:
            return True
    return False

print(double_letters("Helo"))
