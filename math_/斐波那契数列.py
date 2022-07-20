from functools import lru_cache
import sys

sys.setrecursionlimit(5000)


def show_time(old_func):
    import time

    def new_func(*args, **kwargs):
        start_time = time.time()
        new_return = old_func(*args, **kwargs)
        end_time = time.time()
        print(f'{old_func.__name__}耗时{end_time - start_time}秒')
        return new_return

    return new_func


@show_time
def b(n_b: int) -> int:
    @lru_cache(None)
    def a(n: int) -> int:
        """斐波那契数列"""
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return a(n=n - 1) + a(n=n - 2)

    return a(n=n_b)


@show_time
def c(n: int) -> int:
    """前n项求和"""
    all_sum = 0
    for __i in range(n + 1):
        all_sum += __i
    return all_sum


for i in range(1, 700):
    print(i, b(n_b=i))
# print(b(800))
# print(a(10))
# print(c(100))
