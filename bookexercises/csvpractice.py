import csv

with open("data.csv") as f:
    a = csv.reader(f)
    l = []
    for i in a:
        l += i
    print(l)
q = l.index("2005")
q += 1
print("month of 2005 is", l[q])


