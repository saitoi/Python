import json

with open('languages.json', 'r', encoding='utf-8') as jsonfile:
    content = json.load(jsonfile)

    print(type(content))
