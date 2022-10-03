def largest_difference(numbers:list):
    smallest = None
    largest = None
    for number in numbers:
        if smallest is None or smallest > number:
            smallest = number
        if largest is None or largest < number:
            largest = number
    return largest-smallest


print(largest_difference([32, 90, 102, 3, -2]))
