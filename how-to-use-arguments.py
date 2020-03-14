a='a'
b='b'
c='c'



def my_new_function(my_value='hello'):  
  print(my_value)#Calling  
my_new_function() # 打印 hello  
my_new_function('test') # 打印 test



# 任意参数
def myfunc(*arguments):  
  print('args:')
  for a in arguments:  
    print (a) 
myfunc(a)  
myfunc(a,b)  
myfunc(a,b,c)


## 位置参数
def myfunc1(**arguments):  
  return arguments.keys(), arguments.values()

print(myfunc1(a=1,b=2))