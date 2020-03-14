
# 初始化列表
list1 = [0, 1, 2]
list2 = [3,4, 5,]
list3 = [6, 7, 8, 9]

# 1. 通过 + 运算直接拼接
print('# 1. 通过 + 运算直接拼接')
result = list1 + list2 + list3
print(result)



# 2. 通过循环调用list.append()拼接
print('# 2. 通过循环调用list.append()拼接')
result = []
for element in list1:
    result.append(element)

for element in list2:
    result.append(element)

print(result)


# 3. 通过列表表达式拼接
print('# 3. 通过列表表达式拼接')
result = [element for lis in [list1, list2 , list3] for element in lis]

print(result)


# 4. 通过 '*' 解构方式实现拼接

print('4. 通过 '*' 解构方式实现拼接')
result = [*list1, *list2]

print(result)


# 5. 通过内置的extend方法实现拼接
print('# 5.通过内置的extend方法实现拼接')
result = []
result.extend(list1) # list_one contains all the elements
result.extend(list2)
result.extend(list3)

print(result)


# 6. 通过itertools.chain()实现拼接
print('6. 通过itertools.chain()实现拼接')
import itertools

result = list(itertools.chain(list2, list2, list3))
print(result)
