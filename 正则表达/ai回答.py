import re

# {face:8}别发这么无聊的信息行不
m = '{face:8}别发这么无聊的信息行不'

n = re.sub('\{[a-z0-9]+:[a-z0-9]+}', '', m)
print(n)
