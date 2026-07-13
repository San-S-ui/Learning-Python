# '''
# 将函数作为参数传递
# '''
# def func (sum):
#     res = sum(1,3)
#     return res
# def com(x,y):
#     return x+y
# print(func(com))

'''
lambda匿名函数
无名称只可以使用一次
lambda a,b :  a+b  可以不用写return语句
'''
def func (sum):
    res = sum(1,3)
    return res
print(func(lambda x,y:x+y))
