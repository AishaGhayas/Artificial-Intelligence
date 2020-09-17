import json

l = [1,2,3]
d = {1: "a", 2: "b", 3: "c"}
with open("JSONfile.json", "w") as f:
    #json.dump(l, f)
    json.dump(d, f)
with open("JSONfile.json") as f:
    a = json.load(f)
    print(a)
    print(a["2"])
