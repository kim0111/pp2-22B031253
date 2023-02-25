import re

with open("row.txt", "rt+", encoding="UTF-8") as file:
    for lines in file:
        if re.search("ab{2,3}[^b]", lines):
            print(lines)