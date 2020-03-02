# 拼接
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]

# append方式
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)

# 列表推导式
def test3():
    list1 = [i for i in range(1000)]


# 强制转换
def test4():
    list1 = list(range(10000))

import timeit

t1 = timeit.Timer('test1()', 'from_main_import test1')
print(t1.timeit(number=1000))


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()


