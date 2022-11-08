s = 0
for i in range(5):
    s += 2
    print(f"\ni={i}, s={s}")
    if s == 8:
        continue
    print("this line will be skipped")
