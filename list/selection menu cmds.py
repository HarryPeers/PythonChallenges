import sys

global l
global target

l = [int(item.strip()) for item in input("Please enter a list of numbers, seperated by a comma (,)\n    ").split(",")]
target = int(input("Please enter your target number\n    "))


cmds = [
    "1) Target presence check",
    "2) Smallest number",
    "3) Largest number",
    "4) Sum of the numbers",
    "5) Product of the numbers",
    "6) Order the list ascending",
    "7) Order the list descending",
    "8) Exit"
    ]

products = l[0]
for num in l[1:]:
    products *= num

funcs = [
    "Number is in the list" if target in l else "Number is not in the list",
    sorted(l)[0],
    max(l),
    sum(l),
    products,
    ", ".join([str(x) for x in sorted(l)]),
    ", ".join([str(x) for x in sorted(l, reverse=True)])
    ]

while True:
    cmd = input("Please select one of the commands.\n    "+"\n    ".join(cmds)+"\n        ")

    try:
        cmd = int(cmd)
    except:
        print("Please enter a number", file=sys.stderr)
        continue

    if cmd > len(cmds):
        print("Please enter a valid command", file=sys.stderr)
        continue

    if cmd == 8:
        break

    print(funcs[cmd-1])
