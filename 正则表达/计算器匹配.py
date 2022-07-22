import re


def main():
    msg = input(':').strip().replace('\r\n','').replace('\n','').replace('（','(').replace('）',')').replace('，',',').replace('/计算', '')
    print(msg)
    require = "(\d| |\+|\-|\*|/|\(|\)|abs\(|sqrt\(|factorial\(|%|E|e|\.|log\(|\,|j)*"
    if msg != re.match(require, msg, flags=0).group() or "**" in msg:
        print("错误：输入算式中含有非法格式，请使用/计算帮助查询规范。")


if __name__ == '__main__':
    main()
