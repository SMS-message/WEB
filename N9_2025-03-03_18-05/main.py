import requests
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("host", nargs=1)
parser.add_argument("port", nargs=1)
parser.add_argument("jsonl_file", nargs=1)
parser.add_argument("--letters", type=str, default="")
parser.add_argument("--n", type=int, default=1)

args = parser.parse_args()
url = f"http://{args.host[0]}:{args.port[0]}"

with open("stone.jsonl", mode="r", encoding="utf-8") as jsonl_file:
    data = jsonl_file.read().split("\n")
    data = list(filter(lambda jsn: jsn, data))
    response = requests.get(url).json()

    for json_file in data:
        json_data = json.loads(json_file)

        approved_lists = []
        for lst in response:
            approved = []
            for string in lst:
                for i in range(len(json_data["nature"]) - 1):
                    sub_str = json_data["nature"][i:i + 2].lower()
                    if sub_str in (string.lower() + args.letters.lower()):
                        approved.append(True)
                        break
            if all(approved) and approved and len(approved) == len(lst):
                if (len(lst) >= json_data["size"]) and (len(lst) % args.n == 0):
                    approved_lists.append(lst)
        if approved_lists:
            result_list = approved_lists[-1]
            print(f"{json_data['name']}:", ". ".join(result_list))
