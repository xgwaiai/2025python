# 作者: 浙大 浩宇
# 2024年12月31日10时42分52秒


def open_r():
    """
    读取文件
    :return:
    """
    file = open("file2.txt", mode='r', encoding='utf-8')  # 打开文件，mode='r'表示读，encoding='utf-8'表示编码格式为utf-8
    # file = open("file2.txt", mode='r', encoding='gbk') # gbk会导致中文乱码
    text = file.read()  # 读出来的全是字符串
    print(text)
    file.write("world")  # 写入文件，写入失败，因为文件只读‘r’
    file.close()  # 关闭文件, 释放资源


def open_rw():
    """
    读取文件
    :return:
    """
    file = open("file2.txt", mode='r+', encoding='utf-8')  # 使用r+模式打开文件后光标在文件开头，写文件直接覆盖原文件内容
    text = file.read()  # 读出来的全是字符串
    print(text)
    file.write("world")  # 写入文件,写在文件末尾
    file.close()  # 关闭文件, 释放资源


def open_w():
    """
    练习w模式打开文件，如果文件不存在，则创建文件,如果文件存在，则清空文件内容
    只能写不能读，如果使用read()会报错
    :return:
    """
    file = open("file3", mode='w', encoding='utf-8')
    file.write("hello坚持学习")
    file.close()


def open_a():
    """
    练习a模式打开文件，如果文件不存在，则创建文件,如果文件存在，则在文件末尾追加内容
    :return:
    """
    file = open("file1", mode='a', encoding='utf-8')
    file.write("how")
    file.close()


def use_readline():
    """
    使用readline()方法读取文件，每次读取一行内容
    :return:
    """
    file = open("file2.txt", encoding='utf-8')

    while True:
        # 读取一行内容
        text = file.readline()

        # 判断是否读到内容，读取到文件末尾时返回空字符串
        if not text:
            break

        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end="")

    # 关闭文件
    file.close()


if __name__ == '__main__':
    # open_r()
    open_rw()
    # open_w()
    # open_a()
    # use_readline()