import csv
from math import floor
from json import dumps

lst = []
names = []

with open('ownership.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quotechar='"')
    for n, row in enumerate(reader):
        if n == 0:
            continue
        name, prop, num, loc = row[1:]
        num = int(num)
        if name not in names:
            names.append(name)
            dct = {"name": name, "locations": [loc], "properties": [prop], "sum": num, "count": 1}
            lst.append(dct)
            continue
        for i in lst:
            if i["name"] == name:
                dct = i
        dct["locations"].append(loc)
        dct["properties"].append(prop)
        dct["sum"] += num
        dct["count"] += 1

with open("owners.jsonl", mode="w", encoding="utf-8") as jsonl_file:
    for dct in lst:
        for key in ["properties", "locations"]:
            dct[key] = sorted(dct[key])
        dct["ave_number"] = floor(dct["sum"] / dct["count"])
        dct.pop("sum")
        dct.pop("count")

    jsonl_file.write("\n".join(map(dumps, lst)))
