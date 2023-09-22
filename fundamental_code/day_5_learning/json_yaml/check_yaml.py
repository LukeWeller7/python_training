import os
import sys
import yaml


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
        print("Yaml is VALID!")
    else:
        print(f"{sys.argv[1]} not found")

else:
    print("Usage: python check_yaml.py <file>")
