import re

def replace(st):
    return st.group(1).lower()


s = "AbcDefGht"
s = re.findall("[A-z][^A-Z]*", s)
s = re.sub("([A-z])", replace, "_".join(s))
print(s)
