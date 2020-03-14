frameworks = ['flask', 'pyramid', 'scrapy', 'django']  # list

# 打印列表
print('打印列表:')
for frw in frameworks:
    print("Python framework : %s" % frw)


# 打印索引和列表值
print('打印索引和列表值:')
for k,v in enumerate(frameworks):
    print("index: %d   framework : %s" % (k, v))