def choose_print_color(__color: str):

    if __color == 'B':
        def choose(__old_func):
            def new_func(__str: str):
                str1 = '\033[1;34m' + __str + '\033[0m'
                __old_func(str1)

            return new_func
    elif __color == 'R':
        def choose(__old_func):
            def new_func(__str: str):
                str1 = '\033[1;31m' + __str + '\033[0m'
                __old_func(str1)

            return new_func
    else:
        def choose(__old_func):
            def new_func(__str: str):
                str1 = '\033[1;37m' + __str + '\033[0m'
                __old_func(str1)

            return new_func
    return choose


@choose_print_color('B')    # B为打印蓝色，R为红色，其他的则为白色
def new_print(__str: str):
    print(__str)


new_print('hello')

