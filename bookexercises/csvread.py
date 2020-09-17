import csv
with open("potions.csv") as f:
    contents = csv.reader(f)
    data = []
    for i in contents:
        data += i
    print(data)
ind = data.index("Draught of Peace")
ind += 1
print("effect Draught of Peace is ", data[ind])
