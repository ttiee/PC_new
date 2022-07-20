import re

email = input('请输入邮箱地址：')
if re.match(r'^[-._a-zA-z\d]+@[\da-zA-Z]+\.(com|com\.cn|cn)$', email):
    print('符合要求')
else:
    print('不符合')
