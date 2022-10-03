with open("files/data.csv", "r") as file:
    data = file.readlines()
    for line in data:
        segments = line.split(",")
        print(f"Handle:\n    {segments[0]}\nScore:\n    {segments[1]}")
