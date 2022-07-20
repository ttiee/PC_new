class Person:
    country = 'Chinese'

    def __init__(self, name=None, lover=None):
        self.name = name
        self.lover = lover

    def say(self):
        print(self.name)
        return self

    def say_hello(self):
        print(f'hello!My name is {self.name}')
        return self

    def go(self):
        print(f'{self.name}正在走路')
        return self

    def switch_to_lover(self):
        print('转换完成')
        return self.lover

    @classmethod
    def drive(cls):
        print(f'{cls.country} driver正在开车')


Person().drive()
p2 = Person('bb')
p2.lover = p2
p1 = (
    Person('aa', p2)
        .say()
        .say_hello()
        .go()
        .switch_to_lover()
        .say()
        .say_hello()
        .go()
)
