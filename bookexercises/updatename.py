with open("name.txt", "w") as f:
    f.write("hello")
with open("name.txt", "a") as f:
    f.write("Aisha")
with open("name.txt") as f:
    print(f.read())
