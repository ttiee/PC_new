

class Print(str):

    def __call__(self, *args, **kwargs):
        print('hubby')
        return 'hhh'

    def __repr__(self):
        print('repr')
        return 'cui'

    def __int__(self):
        return 0

    @property
    def d6(self):
        print('6d')
        return 'hh, d6'

print(int(Print()))

print(Print()())
print(Print().d6)