import random

print('random numbers between 0 and 9')
for i in range(10):
    print(random.randrange(10))  # 0-9

print('random numbers between 10 and 19')
for i in range(10):
    print(random.randrange(10, 20))  # 10-19


from secrets import randbelow
print('use secrets library to generate random numbers')
for _ in range(10):
    print(randbelow(10))