import os
import sys
# 获取某个目录下面的所有文件
def get_all_file(path, ext='*'):
    filepaths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if ext == '*' or name.endswith(ext):
                filepaths.append(os.path.join(root, name))
    return filepaths

def get_all_dir(path):
    dirpaths = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            dirpaths.append(os.path.join(root, name))
    return dirpaths


if __name__ == '__main__':
    print(get_all_file(sys.argv[1]))
    print(get_all_file(sys.argv[1], '.py'))
    print(get_all_dir(sys.argv[1]))

    print(os.listdir(sys.argv[1]))