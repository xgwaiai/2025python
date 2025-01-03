# 作者: 浙大 浩宇
# 2024年12月31日16时08分27秒

import os
def read_conf():
    """
    读取配置文件
    :return:
    """
    file=open('file4','r+',encoding='utf-8')
    test_info=file.read()
    print(test_info) # 这是一个字符串
    my_dict=eval(test_info)
    print(type(my_dict))
    # print(eval(test_info)) # 不能这么写，会报错
    file.close()

if __name__ == '__main__':
    # read_conf()
    # os.system('rm -rf dir4')
    # os.system('ls')
    eval("__import__('os').system('ls')") # 不要用eval执行前端发来的任何命令，会有安全风险