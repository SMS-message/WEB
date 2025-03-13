import requests
import json
from math import floor
import csv

with open("hares.json", mode="r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    url = f"http://{json_data['host']}:{json_data['port']}/"
    response = requests.get(url).json()

    result = [["no", "difference", "div", "max", "fraction"], ]

    for index, lst in enumerate(response, 1):
        temp_list = []
        filtered = list(filter(lambda i: len(str(i)) == json_data["digits"] and i % 3 != json_data["mod3"], lst))
        if not filtered:
            continue
        temp_list.append(index)
        temp_list.append(max(filtered) - min(filtered))
        temp_list.append(sum(filtered) // 5)
        temp_list.append(max(filtered))
        temp_list.append(floor((len(filtered) / len(lst)) * 100))
        result.append(temp_list)

    with open("leisure.csv", mode="w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"')
        writer.writerows(result)
