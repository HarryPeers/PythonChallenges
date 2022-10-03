def flatten(array:list):
    new = []
    for x in array:
        if type(x) == list:
            for value in x:
                if type(value) == list:
                    new += flatten(value)
                else:
                    new.append(value)
        else:
            new.append(x)
    return new


new = flatten(
    [[3, 0], 2, [[12, 32], 90, 32]]
    )

print(new)
