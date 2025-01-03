# 作者: 浙大 浩宇
# 2024年12月31日09时46分17秒

import random
# import module1
from module1 import test1
from module2 import test1 as module2_test1

test1()
module2_test1()

print(random.__file__)  # 查看模块的路径
a = random.randint(1, 3)  # 调用模块内的函数
print(a)


def main():
    pass


# 别人导入该py文件时，是不会导入main()函数的，只有自己运行该py文件时，才会执行main()函数
if __name__ == '__main__':
    main()
