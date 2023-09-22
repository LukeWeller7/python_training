# Scripting

# There are seven modules that we can consider "core" in Python.

import sys
import os
import math
import subprocess
import random
import datetime
import json


# sys

# print(sys.version)

# os

# print(os.getcwd())


# subprocess

subprocess.run(["python", "hello_world.py"]) # Runs other programs in dir

#

print(math.pi)
print(math.sqrt(2))

# random

r = random.randint(0, 100)

print(f"{r}%")

# datetime

print(datetime.datetime.now())

# json


