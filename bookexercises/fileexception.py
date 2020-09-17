while True:   
    try:
        n = input("enter file name: ")
        with open(n) as f:
            print("its open")
            break
    except FileNotFoundError:
        print("sorry")
