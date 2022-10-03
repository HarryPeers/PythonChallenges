def read(file:str, *args) -> list[str]:
    with open(f"./{file}") as file:
        return file.readlines()

def write(file:str, data:str):
    with open(f"./{file}", "w") as file:
        file.write(data)

def append(file:str, data:str):
    with open(f"./{file}", "a") as file:
        file.write("\n"+data)

file = "files/file.txt"

print(read(file, "banana"))
