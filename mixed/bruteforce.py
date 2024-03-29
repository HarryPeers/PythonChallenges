from threading import Thread

def guess(interval:int):

    password = "PDvgIo"

    characters = "abcdefghijklmnopqurstvwxyz"
    characters_upper = characters.upper()

    characters = list(characters) + list(characters_upper)

    characters_mapped = {}
    index = 0

    for character in characters:
        characters_mapped[character] = index
        index += 1
        

    length = 1

    cracked = list(length*characters[0])
    total = len(characters_mapped) - 1
    index = len(cracked)-1
    finished = False

    while True:
        for x in range(0,1000000):
            if "".join(cracked) == password:
                print(f"       Cracked password! {''.join(cracked)}")
                finished = True
                break

            
            if cracked[-1] == characters[-1]:
                carry_on = False
                for x in range(len(cracked)):
                    working_index = len(cracked)-x-1
                    if cracked[working_index] != characters[-1] and carry_on:
                        try:
                            cracked[working_index] = characters[characters_mapped[cracked[working_index]]+interval]
                        except:
                            carry_on=True
                            increase_length = True
                        break
                    elif cracked[working_index] == characters[-1]:
                        carry_on = True

                        increase_length = True
                        for character in cracked:
                            if character != characters[-1]:
                                increase_length = False

                        if increase_length:
                            length += 1
                            
                            cracked = list(length*characters[0])
                            total = len(characters_mapped) - 1
                            index = len(cracked)-1


                        else:
                            cracked[working_index] = characters[0]

                        

                continue

            cracked[index] = characters[characters_mapped[cracked[index]]+1]
            
        if finished:
            break
        else:
            print("".join(cracked))


guess(1)

input()
    
