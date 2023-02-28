def wrapper():
    num = 100

    def inner():
        print(num)

    return inner


inner = wrapper()
inner()

