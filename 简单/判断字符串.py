import re

'''
O
'''


def main():
    print('0'.isdigit(), '10.0'.isdigit(), '1.4'.isdigit(), '-1'.isdigit(), '-1-'.isdigit())
    print('100'.isdigit())


def main2():
    # 判断字符串是否是数字(数字、小数、负数、负小数、O)
    # 字符串
    str_numbers = ["-0.3", "o", "2", "0.002", " - 5", " china", "中国", "-like", "-中国", '1.1.3']
    for str_number in str_numbers:
        if (str_number.split(".")[0]).isdigit() or str_number.isdigit() or (str_number.split("-")[-1]).split(".")[-1].isdigit():
            print(str_number + "是数字")
        else:
            print(str_number + "不是数字")


if __name__ == '__main__':
    main()
    main2()
