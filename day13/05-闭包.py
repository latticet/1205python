def wrapper():
    num = 100

    def inner():
        print(num)

    return inner


my_inner = wrapper()
my_inner()


def wrapper(num):
    def inner():
        print(num)

    return inner


my_inner = wrapper(10)
my_inner()
