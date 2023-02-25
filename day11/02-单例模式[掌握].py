# 单例设计模式
# 说明：一个类只能创建一个对象

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        """
        if cls.instance:
            return cls.instance
        else:
            cls.instance = super().__new__(cls, *args, **kwargs)
            return cls.instance
        """

        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


# 调用
single1 = Singleton()
single2 = Singleton()
single3 = Singleton()
print(single1)
print(single2)
print(single3)
