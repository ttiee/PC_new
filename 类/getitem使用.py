class Do:
    def __init__(self, name):
        self.name = name

    def print_hi(self):
        print(f'Hi, {self.name}')

    def __getitem__(self, item):
        return self.name


def main():
    a1 = Do('uy')
    print(a1[3])


if __name__ == '__main__':
    main()
