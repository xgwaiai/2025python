# 作者: 浙大 浩宇
# 2024年12月31日16时00分02秒


import sys

# print(type(sys.argv))
print(sys.argv)
def write_hello(file_path):
    """
    # python如何传参
    :param file_path:
    :return:
    """
    file=open(file_path,'w+',encoding='utf-8')
    file.write('hello')
    file.close()

if __name__ == '__main__':
    write_hello(sys.argv[1])
