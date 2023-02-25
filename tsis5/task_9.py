import re

s = "AbcDefGht"
s = re.findall("[A-Z][^A-Z]*", s)
print(' '.join(s))
