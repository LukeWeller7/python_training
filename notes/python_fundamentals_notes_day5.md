# JSON

#### Parsing is making something (more) understandable. So let's make json more understandable for Python.
```python
import json
import sys


parsed_json = json.loads(open("example_json.json").read())
print(type(parsed_json))
value = parsed_json["name"]
print(value)

print("Json information")
for keys in parsed_json:
    print(f"This is the Key: {keys} This the value: {parsed_json[keys]}")
```

### Bonus
```python
user_json_file = sys.argv[1]
user_json = json.loads(open(user_json_file).read())
print(f"Json information from {user_json_file}")
for keys in user_json:
    print(f"{keys} : {user_json[keys]}")


```
## Check JSON
```python
import os
import sys
import json


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is VALID!")
    else:
        print(f"{sys.argv[1]} not found")

else:
    print("Usage: python check_json.py <file>")
```

## JSON to Yaml

```python
import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No file, no usage
else:
    print("Usage: json2yaml.py <source_file.json> [target_file.yaml]")

# Processing the conversion
output = yaml.dump(source_content)

# If no target file send to stdout
if len(sys.argv) < 3:
    print(output)
# If the target file already exists exit
elif os.path.exists(sys.argv[2]):
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)
# Otherwise write to the specified file
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()

```
