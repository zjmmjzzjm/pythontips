import os

# 获取某个目录下面的所有文件
def get_all_file(path, ext='*'):
    filepaths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if ext == '*' or name.endswith(ext):
                filepaths.append(os.path.join(root, name))
    return filepaths

# 获取两个字符串的公共前缀
def get_prefix(str1, str2):
    maxIndex = -1
    for k in range(len(str1)):
        if k >= len(str2):
            break
        if not str1[k] == str2[k]:
            break
        maxIndex = k
    if maxIndex != -1:
        return str1[:maxIndex + 1]
    return ''

# 获取列表中字符串的公共前缀
def get_prefix_of_list(strs):
    if len(strs) == 0:
        return ''
    prefix = strs[0]
    for k in range(1, len(strs)):
        prefix = get_prefix(prefix, strs[k])
    return prefix

# 去掉前缀，重新命名
def rename_file_with_prefix(filelist):
    basenames = [os.path.basename(f) for f in filelist]
    print(basenames)
    prefix = get_prefix_of_list(basenames)
    for filename in filelist:
        dirname = os.path.dirname(filename)
        basename = os.path.basename(filename)
        target = basename.replace(prefix[:-1], '')
        os.rename(filename, os.path.join(dirname, target))

if __name__ == '__main__':
    target_dir = '/Users/zjm/Workspace/download/bili/侯宝林'
    filelist = get_all_file(target_dir)
    rename_file_with_prefix(filelist)
    print(os.listdir(target_dir))