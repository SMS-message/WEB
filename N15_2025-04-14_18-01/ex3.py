import requests

address = "http://127.0.0.1:"

port = input()
word = input()
length = int(input())

address += port

data = requests.get(address).json()

my_dct = dict()

for dct in data:
    tale = dct["tale"]
    if word in tale or dct["duration"] > length:
        continue

    for tag in dct["tags"].split(", "):
        if tag in my_dct:
            my_dct[tag].append(tale)
        else:
            my_dct[tag] = [tale]

res = {}

for i in sorted(my_dct):
    res[i] = my_dct[i]

for i, j in res.items():
    print(f"{i}: " + ". ".join(sorted(set(j), reverse=True)))
