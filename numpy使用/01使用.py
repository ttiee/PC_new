import numpy as np


def a_01():
    """对角"""
    arr = np.eye(4)
    print(arr)
    print(arr.ndim)
    print(arr.shape)
    print(arr.size)


def a_02():
    a = np.array([1, 2, 3])
    print(a)
    print(type(a[0]))
    print(a[0])


# print([0, 1, 2])


def a_03():
    b = np.array([[1, 2], [3, 4]])
    print(b)


def a_04():
    a = np.array([1, 2, 3, 4, 5], ndmin=2)
    print(a)


def a_05():
    a = np.array([1, 2, 3], dtype=complex)
    print(a)


def a_06():
    dt = np.dtype(np.int32)
    print(dt)


def a_07():
    dt = np.dtype([('age', np.int8)])
    print(dt)


def a_08():
    dt = np.dtype([('age', np.int8)])
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print(a)
    print(a['age'])
    print(type(a[0][0]))


def a_09():
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    print(a)
    print(a['name'])
    print(a.ndim)
    print(a.shape)
    print(a.size)


def a_10():
    a = np.arange(24)
    print(a)
    print(a.ndim)  # a 现只有一个维度
    # 现在调整其大小
    b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
    print(b)
    print(b.ndim)


def a_11():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    a.shape = (3, 2)
    print(a)


def a_12():
    # 数组的 dtype 为 int8（一个字节）
    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    print(x.itemsize)

    # 数组的 dtype 现在为 float64（八个字节）
    y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print(y.itemsize)


def a_13():
    x = np.array([1, 2, 3, 4, 5])
    print(x.flags)


def a_14():
    a = np.array([[1, 2, 3], [4, 5, 6]], copy=False)
    b = a.reshape(6,)
    c = a.copy()
    b[0] = 100
    print(b)
    print(a)
    c[0] = 99
    print(c)
    print(a)
    print(b)


def a_15():
    x = np.empty([3, 2], dtype=int, order='C')
    print(x)


if __name__ == '__main__':
    a_15()
