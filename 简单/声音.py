from winsound import Beep
import random
import time


def beep_print(h, t):
    Beep(h, t)
    print(f'{h}持续{t}毫秒')


def for_mu():
    for i in range(100, 3_7000):
        beep_print(i, 500)


def rand_mu():
    while 1:
        beep_print(random.randint(1000, 4000), random.randint(300, 500))
        time.sleep(0.1)

        beep_print(random.randint(500, 2000), random.randint(300, 500))
        time.sleep(0.1)


if __name__ == '__main__':
    rand_mu()