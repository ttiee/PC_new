import random


def main(num):
    difference = float('inf')

    data = [random.randint(0, 999) for _ in range(200)]
    s_data = sorted(list(set(data)))

    for _, _a in enumerate(s_data[:-1]):
        for b in s_data[_ + 1:]:
            difference = min(abs(num - _a - b), difference)
            if abs(num - _a - b) == 0:
                print(_a, b)

    print(s_data)
    print(difference)


if __name__ == '__main__':
    main(500)
    # a()
    ...


def subset(A: list) -> list:  # 求集合的所有子集
    N = len(A)
    Subset = []
    for i in range(2 ** N):
        b = []
        for j in range(N):
            if (i >> j) % 2 == 1:  # 关键：判断该位是否为1
                b.append(A[j])
                if b not in Subset:
                    Subset.append(b)
    return Subset


def sum_subset(S: list) -> None:  # 求子集和
    for i in S:
        if sum(i) == 5:
            print(i)


if __name__ == "__main__":
    # A = [random.randint(0, 10) for _ in range(10)]
    # S = subset(A)
    # sum_subset(S)
    ...


def a():
    import numpy as np
    # A Dynamic Programming solution for subset sum problem
    # Returns true if there is a subset of set with sum equal to given sum
    def isSubsetSum(S, n, M):
        # The value of subset[i, j] will be
        # true if there is a subset of
        # set[0..j-1] with sum equal to i
        subset = np.array([[True] * (M + 1)] * (n + 1))
        # If sum is 0, then answer is true
        for i in range(0, n + 1):
            subset[i, 0] = True
        # If sum is not 0 and set is empty,
        # then answer is false
        for i in range(1, M + 1):
            subset[0, i] = False
        # Fill the subset table in bottom-up manner
        for i in range(1, n + 1):
            for j in range(1, M + 1):
                if j < S[i - 1]:
                    subset[i, j] = subset[i - 1, j]
                else:
                    subset[i, j] = subset[i - 1, j] or subset[i - 1, j - S[i - 1]]
        # print the True-False table
        for i in range(0, n + 1):
            for j in range(0, M + 1):
                print('%-6s' % subset[i][j], end="  ")
            print(" ")
        if subset[n, M]:
            print("Found a subset with given sum")
        else:
            print("No subset with given sum")

    # test
    st = [1, 3, 4, 5]
    n = len(st)
    sm = 7
    isSubsetSum(st, n, sm)
