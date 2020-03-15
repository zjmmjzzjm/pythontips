
# pop
li = ['baidu', 'sina','tencent', 'google', 'ali']
result = li.pop(1)
print(li, result)

result = li.pop() # 删除最后一个元素
print(li, result)

# del 
li = ['baidu', 'sina','tencent', 'google', 'ali']
del li[1]
print(li)

del li[0:2]
print(li)


# remove
li = ['baidu', 'sina','tencent', 'google', 'ali']
li.remove('baidu')
print(li)

# clear
li.clear()
print(li)