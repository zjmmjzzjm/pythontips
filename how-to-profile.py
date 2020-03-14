import cProfile, pstats 
from io import StringIO
pr = cProfile.Profile() 
pr.enable() 
# 做一些运算操错
st=''
for k in range(1000):
    for j in range(1000):
        st += ' {} -> {}'.format(k + j, j*k) 

   
pr.disable() 
s = StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative') 

ps.print_stats()
ps.print_callers()  # 显示函数被哪些函数调用
ps.print_callees()  # 显示哪个函数调用了哪些函数
print(s.getvalue())


# 解释:
# ncalls：表示函数调用的次数；
# tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
# percall：（第一个percall）等于 tottime/ncalls；
# cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
# percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
# filename:lineno(function)：每个函数调用的具体信息；
# 需要注意的是cProfile很难搞清楚函数内的每一行发生了什么，是针对整个函数来说的。

# https://www.cnblogs.com/c-x-a/p/10264490.html