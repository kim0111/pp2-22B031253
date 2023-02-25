import re

s = "Hello_my_friend"


def replace(st):
    return st.group(1) + st.group(2).upper()

s = re.sub("(.?)_([a-z])", replace, s)
print(s)