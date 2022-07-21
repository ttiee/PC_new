import re


def main():
    pattern = r'[0-9]{1,3}(\.[0-9]{1,3}){3}'
    str1 = '127.0.0.9 192.198.1.66'
    ma = re.findall(pattern, str1)
    print(ma)


if __name__ == '__main__':
    main()
