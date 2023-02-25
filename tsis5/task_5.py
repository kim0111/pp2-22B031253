import re

with open("row.txt", "rt+", encoding="UTF-8") as file:
    for lines in file:
        if re.search("a.*b$", lines):
            print(lines)