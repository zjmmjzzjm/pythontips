
from configparser import ConfigParser
from io import StringIO

# 实例化
config = ConfigParser()

# 读取ini文件
config.read('assets/test.ini')

# 读取section和值
string_val = config.get('section_1', 'string_val')
bool_val = config.getboolean('section_1', 'bool_val')
int_val = config.getint('section_1', 'int_val')
float_val = config.getfloat('section_1', 'pi_val')

print('string_val: {}\nbool_val: {}\nint_val: {}\nfloat_val: {}'.format(string_val, bool_val, int_val, float_val))
# 更新值
config.set('section_1', 'string_val', 'world')
s = StringIO()
config.write(s)
print('# 更新值\n', s.getvalue())


# 增加一个新的section
config.add_section('section_2')
config.set('section_2', 'meal_val', 'spam')
config.set('section_2', 'not_found_val', '404')
s = StringIO()
config.write(s)
print('# 增加一个新的section\n', s.getvalue())


# 删除一个值
config.remove_option('section_1', 'bool_val')
config.remove_section('section_0')
s = StringIO()
config.write(s)
print('# 删除一个值\n', s.getvalue())

# 保存至文件
with open('tmp/test_update.ini', 'w') as configfile:
    config.write(configfile)

