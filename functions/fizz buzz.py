for x in range(1,51):
    five = x % 5
    three = x % 3
    if x%3 == 0 and five == 0:
        print("FizzBuzz")
    elif three == 0:
        print("Fizz")
    elif five == 0:
        print("Buzz")
