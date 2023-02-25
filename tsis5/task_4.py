import re

with open("row.txt", "rt+", encoding="UTF-8") as file:
    for lines in file:
        if re.search("[A-Z][a-z]", lines):
            print(lines)