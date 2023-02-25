def fn1():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(e)


def fn2():
    fn1()


def fn3():
    fn2()


fn3()
