# Parsing is making something (more) understandable. So let's make json more understandable for Python.

import json
import sys


parsed_json = json.loads(open("example_json.json").read())
print(type(parsed_json))
value = parsed_json["name"]
print(value)

print("Json information")
for keys in parsed_json:
    print(f"This is the Key: {keys} This the value: {parsed_json[keys]}")


# Bonus
user_json_file = sys.argv[1]
user_json = json.loads(open(user_json_file).read())
print(f"Json information from {user_json_file}")
for keys in user_json:
    print(f"{keys} : {user_json[keys]}")
