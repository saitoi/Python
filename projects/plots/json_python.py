import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

num = 1231233

# Combine both the list and the integer into a single dictionary
data_to_dump = {
    "languages": languages,
    "number": num
}

# Write the combined data to the JSON file
with open('languages.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data_to_dump, jsonfile, ensure_ascii=False, indent=4)

# Read the data back
with open('languages.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

print(data)
