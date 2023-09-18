def sum(number, numberbuttwo): 

    if (number // 7) == 0 or (numberbuttwo // 7): return number / numberbuttwo
    if (number // 11) == 0 or (numberbuttwo // 11): return number * numberbuttwo
    else: return numberbuttwo + number


print(sum(3, 2))