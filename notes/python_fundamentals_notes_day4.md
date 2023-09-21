# What is scripting and why Python?

### Why is Python so popular?

- Easy to learn
- Active and supportive community
- Flexible
- Efficient, fast, adn reliable
- Academic language (Lots of learning resources)
- Concise and Readable
- Multi-platform

### What are some different areas Python is used?

- Ai & machine learning
- Data visualisation
- Game development
- Web development
- Multi-dimensional design (2D, 3D, 4D)
- Data Science
- Academic

### Who is using Python (examples of companies please).

- Sparta Global
- Intel
- Netflix
- Facebook
- Spotify
- Youtube (Google)

### Why is Python used in DevOps?

- Because it is the most popular coding language that provides flexibility and accessibility. Due to its simplicity and extensive library support, this makes python a must for DevOps

### What is a script? And how are they different to Programs?

- Scripts are typically a few lines of code, which is found within a program. The scripts are used to automate a particular part of the code to perform tasks within the program.

### Why are scripts useful? What is their main purpose?

- Scripting is often easier to learn that programming and is generally used for web & app development.

### Why use Python for scripting?

- Because Python is easy to learn, with a syntax that is easy to understand. Focusing on readability through its libraries and modules providing code to be reused.

### Bonus: Can you find 10 examples of  useful Python scripts for a DevOps engineer?

- **Requests** - making it possible to retrieve live data for HTTPS
- **PDF to Audio File** - using PyPDF to read text from PDFs and Pyttsx3 which allows python to convert to text to speech
- **Boto3** - The equivilant of AWS for Python.
- **Subprocess Module** - To allow DevOps to run external program and read the output in Python.
- **OS Module** - Allowing interacting with operating systems to create/remove directories as well as seeing what exists.
- **GetPass/GetUser Module** - To ask the user for the password without echoing it.
- **GitHub API** - Better management with creating, deleting, and listing GitHub repos.



# Scripting
There are seven modules that we can consider "core" in Python.

```python
import sys
import os
import math
import subprocess
import random
import datetime
import json


# sys

print(sys.version)

# os

print(os.getcwd())


# subprocess

subprocess.run(["python", "hello_world.py"]) # Runs other programs in dir

# math

print(math.pi)
print(math.sqrt(2))

# random

r = random.randint(0, 100)

print(f"{r}%")

# datetime

print(datetime.datetime.now())

# json
```
