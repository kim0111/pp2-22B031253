import re

with open("row.txt", "rt+", encoding="UTF-8") as file:
    for lines in file:
        if re.search("[,. ]+", lines):
            x = lines
            x = re.sub("[\s.,]+", ";", x)
            print(x)