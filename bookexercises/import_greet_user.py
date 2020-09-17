import greetuser
greetuser.greet("Aisha")
import csv
with open("data.csv") as f:
    a = csv.reader(f)
    l = []
    for i in a:
        l += i
    print(l)
