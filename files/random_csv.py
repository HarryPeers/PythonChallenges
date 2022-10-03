import random

chars = list("abcdefghijklmopqurstvwxyz")

data = []
for x in range(100):
    data.append(f"{''.join([random.choice(chars) for x in range(9)])},{random.randint(111111, 999999)}")

with open("files/data.csv", "w") as file:
    file.write("\n".join(data))
