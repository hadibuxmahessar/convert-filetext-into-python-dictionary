import json

file = open("testtextfile")

# supposed to be dictionary in text file with keys in double quotes
file_data = file.read()

json_data = json.loads(file_data)

print(json_data)

print(type(json_data))
