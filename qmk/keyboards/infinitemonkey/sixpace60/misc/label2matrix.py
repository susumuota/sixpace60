# python label2matrix.py < label.json > matrix.json

import re
import sys

while line := sys.stdin.readline():
    print(re.sub(r'"label"\s*:\s*"(\d+),(\d+)"', r'"matrix": [\1, \2]', line), end="")
