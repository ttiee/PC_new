import datetime


def main():
    with open("data.json", 'r', encoding='utf-8') as f:
        data = f.read()
    with open(f'{datetime.date.today()}_data.json', 'w', encoding='utf-8') as p:
        p.write(data)


if __name__ == '__main__':
    main()
