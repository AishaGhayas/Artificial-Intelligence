import csv

with open("datafile.csv", "w", newline="") as f:
    dh = csv.writer(f, delimiter=",")
    dh.writerow(["y", "m", "d"])
    dh.writerow(["2009", "sep", "1st"])
    dh.writerow(["2010", "oct", "2nd"])

with open("datafile.csv", "a", newline="") as f:
    dh = csv.writer(f, delimiter=",")
    dh.writerow(["y", "m", "d"])
    dh.writerow(["2011", "s", "11"])
    dh.writerow(["2012", "ot", "22"])
    
with open("datafile.csv") as f:
    a = csv.reader(f)
    l = []
    for i in a:
        l += i
    print(l)
