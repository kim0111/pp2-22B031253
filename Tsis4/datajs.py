import json

with open("sample-data.json") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))


