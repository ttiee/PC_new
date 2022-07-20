num1 = 1


def num1_add_1():
    """num1+1"""
    global num1
    num1 += 1
    return num1_add_1


a = (
    num1_add_1()
    ()()()
    ()()
    ()
)
print(num1)