from functools import lru_cache
from fractions import Fraction


@lru_cache(None)
def main(num):
    if num == 2:
        print('2', end='')
        return 2
    else:
        for i in range(2, num.numerator):
            if num % i == 0:
                num = Fraction(num, i)
                print(i, end=' * ')
                return main(num)
        else:
            print(num)


if __name__ == '__main__':
    number = eval(input('请输入需要因数分解的数字:'))
    print(f'{number} =', end=' ')
    main(num=number)
