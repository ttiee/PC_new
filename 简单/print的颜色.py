# 可以根据自己的需求，把常用的封装起来，用的时候直接调用就可以了
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.HEADER + "警告的颜色字体?" + bcolors.ENDC)

print('This is a \033[1;35m test \033[0m!')
print('This is a \033[1;32;43m test \033[0m!')
print('\033[1;33;44mThis is a test !\033[0m')

