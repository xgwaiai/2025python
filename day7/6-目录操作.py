# 作者: 浙大 浩宇
# 2024年12月31日14时41分47秒

import os

def use_rename():
    """
    理解相对路径和绝对路径
    :return:
    """
    # os.rename('file3','file4')
    # os.rename('C:\\python_code2025\\day7\\file4', 'file3') # 绝对路径要用双斜杠
    # os.rename('dir1\\file1','dir1\\file2') # 相对路径
    # os.rename('dir1/file2', 'dir1/file1')  # 相对路径用斜杠
    os.remove('dir1/file1')  # 删除文件


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    # os.mkdir('dir2')
    # os.rmdir('dir1')
    print(os.getcwd())  # 获取当前工作目录
    os.chdir('dir2')  # 修改工作目录
    print(os.getcwd())
    file = open('file1', 'w', encoding='utf8')
    file.write('987654321')
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())
    os.chdir('dir2')  # 表示进到dir2目录下，类似与cd命令
    print(os.getcwd())


def scan_dir(current_path, width):
    """
    目录深度优先遍历
    文件夹就是目录，文件就是文件
    :return:
    """
    file_list = os.listdir(current_path)  # 获取当前目录下的所有文件
    for file in file_list:  # 这里file拿到的是文件名，不是路径
        print(' ' * width, file)  # width代表打印多少个空格
        new_path = current_path + '/' + file  # 路径拼接：当前路径+文件名
        if os.path.isdir(new_path):
            # print(new_path) # 打印目录名
            scan_dir(new_path, width + 4)  # 递归调用，传入新的路径和宽度+4


def use_stat(file_path):
    """
    获取文件信息，包括文件大小，创建时间，修改时间，权限等
    :return:
    """
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)  # 时间是文件创建时间，不是修改时间
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))  # 格式化时间


if __name__ == '__main__':
    # use_rename()
    use_dir_func()
    # change_dir()
    # scan_dir('.',0) # 使用相对路径
    # scan_dir('C:\\python_code2025\\day7',0) # 使用绝对路径
    # use_stat('file1')
