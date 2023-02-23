class Math:
    def __init__(self):
        self.__Pei = 3.141592653

    def get_Pei(self):
        print(self.__Pei)


math = Math()


math.__Pei = 10
print(math.__Pei)

math.get_Pei()



