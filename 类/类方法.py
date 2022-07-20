class A:

    @property
    def say(self):
        print('hhh1')
        return self

    @staticmethod
    def say2():
        print('222')




def main():
    a1 = A()
    a1.say.say.say
    A.say2()


if __name__ == '__main__':
    main()
