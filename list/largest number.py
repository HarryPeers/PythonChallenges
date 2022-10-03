array = []
for x in range(3):
    array.append(int(input(f"Enter number {x+1}:")))

array = sorted(array)

print(f"The largest number is {array[-1]}")
