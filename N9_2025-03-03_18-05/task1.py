import json
import sys

inp = [i.strip() for i in sys.stdin]

dct = {}

for index, string in enumerate(inp):
    situations = [(len(sit.strip()), sit.strip()) for sit in string.split(".")]

    lst = []
    for length_sit, situation in situations:
        for word in situation.split():
            if length_sit % 2 == len(word) % 2:
                lst.append(word)
    if lst:
        dct[f"{index}"] = lst

with open("consolation.json", mode="w", encoding="utf-8") as json_file:
    json.dump(dct, json_file, ensure_ascii=False, indent=2)
