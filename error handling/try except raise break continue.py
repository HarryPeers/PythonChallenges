while True:
    try:
        name = input("Enter your name")
        if name.lower() == "break":
            break
        elif name.lower() == "continue":
            continue
        elif name.lower() == "error":
            raise
        else:
            print(f"Hello {name}")
    except:
        print("error!")
