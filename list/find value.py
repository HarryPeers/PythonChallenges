l = [32, 901, 92, 31, 902]
target = 92
index = 0
found = False
for num in l:
    if num == target:
        print(f"Num found in index {index}")
        found = True
    index += 1

if not found:
    print("Num not found in list")
