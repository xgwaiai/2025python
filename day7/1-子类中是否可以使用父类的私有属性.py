# 作者: 浙大 浩宇
# 2024年12月31日09时15分32秒


class A:
    def __init__(self):
        self.__age = 18

    def base_age(self):
        print(self.__age)


class B(A):
    def __init__(self):
        super().__init__()
    def get_age(self):
        # print(self.__age) # 报错，不能访问父类的私有属性
        self.base_age() #   可以访问父类的公有方法

if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age()




