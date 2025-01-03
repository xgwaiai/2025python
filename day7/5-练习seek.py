# 作者: 浙大 浩宇
# 2024年12月31日11时19分31秒
import os


def seek_start():
    """
    相对于文件开头的偏移量
    :return:
    """

    file = open('file1', mode='r+', encoding='utf-8')
    file.seek(5, os.SEEK_SET)  # 相对于文件开头的偏移量，5表示从第6个字节开始读取，汉字占3个字节，所以汉字偏移是3的倍数
    test = file.read(5)  # 读取5个字符
    print(test)
    file.close()


def seek_end():
    """
    相对于文件结尾的偏移量，偏移量只能填0，相对于当前位置不动
    :return:
    """
    file = open('file1', mode='r+', encoding='utf-8')
    file.seek(0, os.SEEK_END)  # 相对于文件结尾的偏移量，偏移量只能填0
    test = file.read(0)
    print(test)  # 读不到内容，是空字符串
    file.close()


def seek_cur():
    """
    相对于当前位置不动
    :return:
    """
    file = open('file1', mode='r+', encoding='utf-8')
    file.seek(0, os.SEEK_CUR)
    test = file.read(5)
    print(test)  # 读不到内容，是空字符串
    file.close()


def seek_b_cur():
    """
    在b模式下，读取到的是字节流，读取图片、音频、视频等二进制文件时需要用到
    :return:
    """
    file = open('file1', mode='rb+')  # b模式下不需要指定encoding
    file.seek(5, os.SEEK_CUR)
    file.seek(-2, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    b = file.read()  # 得到的是字节流
    print(b)
    file.close()


def copy_file():
    """
    复制文件
    :return:
    """
    file1 = open('pingpang.png', mode='rb+')
    file2 = open('pingpang_copy.png', mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()


def modify_movie():
    """
    修改视频文件
    :return:
    """
    file1 = open('pingpang.png', mode='rb+')
    file1.seek(10, os.SEEK_SET)
    b = file1.read(1)
    inverted_b = bytes([~b[0]&0xff]) # 按位取反后限制在0-255范围内
    # print("取反字节：",inverted_b)
    # print(b)
    file1.seek(10, os.SEEK_SET)

    # 写回取反后的字节
    file1.write(inverted_b)
    # print(b)
    file1.close()


if __name__ == '__main__':
    # seek_start()
    seek_end()
    # seek_cur()
    # seek_b_cur()
    # copy_file()
    # modify_movie()