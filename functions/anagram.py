def is_anagram(a, b):
    characters = list(a)
    for character in b:
        if character not in characters:
            return False
        characters.remove(character)
    if characters != []:
        return False
    return True
                  


a = is_anagram("hello", "lleho")

print(a)
