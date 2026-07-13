#数据容器的类型： list tuple str set dict

'''
列表 List
[ , , , ]
a = []
a = list[]

'''
# a = [1,True,'se']
# b = list[1,2,3,'12']
# c = [[1,'za'],[3,False],2]
# print(a)
# print(b)
# print(c)
# print(type(c))
# print('--------------------------------------------------')
# #下标索引
# a = [3,'str',True]
# b = [[1,2,3],['a','b','c'],[True,False]]
# print(a[-1])
# print(b[-1][1])
'''
常用操作和特点
列表的方法
class Student:
    def func():
        return
方法的调用：
student = Student()
num = student.add(1,2)
1.查找下标
a.index('abc')
2.修改
a[1]='h'
3.插入
a.insert(1,'k')
4.追加一个
a.append('g')
5.追加一堆
a.extend([1,2,'qwe'])
6.删除指定下标
del a[1]
a.pop(2)
7.删除匹配到的某元素内容
a.remove('qwe')
8.清空列表
a.clear() 结果是[]
9. 统计数量
b = a.count('abc')
10.统计多少个元素
len(a)

列表可以增删改查，有索引，可以重复，
元素类型可以不一样，可容纳很多元素
'''
# a = ['abc','def']
# re = a.index('def')
# print(re)# def下标是一
# a[0]='j'
# print(a)
# a.insert(0,'k')
# print(a)
# a.append(10)
# print(a)
# list2 = ['asd']
# a.extend(['qwe'])
# a.extend(list2)
# print(a)
# del a[0]
# print(a)
# b=a.pop(0)
# print(a,end='删除了 ')
# print(b)
# a.remove(10)
# print(a)
# b = a.count('def')
# print(b)
# print(len(a))

#列表的遍历
# #while
# a = ['123','abc',True]
# index = 0
# while index<len(a):
#     b = a[index]
#     print(b,end=' ')
#     index+=1
# #for
# a = ['123','abc',True]
# for i in a:
#     print(i)

"""
元组
可以存储多个不同的类型数据
不可被篡改
a = ( , , )
a = tuple( , , )
如果只有一个数据
a = (123, )
嵌套 如果嵌套了list那么list里面可以修改
a = ((),(),())
方法
index() count() len()
"""
t1 = (1,'qwe',('qwe',True))
# print(t1.count('qwe'))
# t2 = (12, )
# a = t1[2][1]
# print(a)
# print(t1.count('qwe'))
# print(len(t1))

'''
字符串
无法修改
1.index()
2.字符串替换
a.replace(字符串1，字符串2)
将1换为2  得到一个新的字符串
3.分割为多个字符串存入到一个列表中
a.split('a')
4.字符串的规整
a.strip() 去除前后空格
a.strip('a')去除指定字符只删除左右的
5.a.count('a')
6.len(a)
'''
# a = 'asdfgajka'
# print(a.count('a'))
# b = a[-1]
# print(b)
# b = a.index('dfg')
# print(b)
# b = a.replace('a','b')
# print(a)
# print(b)
# b = a.split('a')
# print(b)
# b = a.strip('ak')
# print(b)
# a = ' asd qwe art qsc '
# b = a.strip()
# print(a)
# print (b)
"""
序列的切片，序列都可以切片
序列：连续，有序，可以用下标索引
列表，元组，字符串都是序列
"""

'''
集合 set  不能用a = {}
a = set{ , , }
不可以重复，无序
可以修改
1.添加
a.add()
2.移除
a.remove()
3.随机取
a.pop()
4.清空
a.clear()
5.取差集
c=a.difference(b) a里面有b里面没有的
6.消除差集
a.difference_update(b) a被修改
7.合并
a.union(b)
8.len(a)

'''
# a = {"we","asdf",123}
# print(a)
# a.add(1)
# print(a)
# a.remove(123)
# print(a)
# b = a.pop()
# print(b)
# print(a)
# print('-------------------------------')
# a = {"we","asdf",123}
# b = {'asdf',456}
# c = a.difference(b)
# print(a)
# print(b)
# print(c)
# print('-----------------------')
# a.difference_update(b)
# print(a)
# print(b)
# c=a.union(b)
# print(c)

# #集合的遍历 不可以用while  用for循环
# a = {123,'qwe',False}
# for i in a:
#     print(i)

"""
字典
a = {key:value,key:value}
a = dict{key:value,key:value}
空字典
a = {}
1. key不可以重复
2.无下标
3.key不可是字典
"""
# a = {"小明":99,"小红":76,"小金":56}
# print(a["小红"])
#
# #字典的嵌套
# a = {
#     "小明":{
#         '语文':78,
#         '数学':89,
#         '英语':93
#             },
#     "小红":{
#         '语文':90,
#         '数学':88,
#         '英语':87
#             },
#     "小金":{
#         '语文':76,
#         '数学':65,
#         '英语':60
#             }
# }
# print(a)
# print(a['小红'])
# print(a['小红']['数学'])
"""
字典常用操作
1.新增和更新
a[] = key
2.删除
a.pop()
3.清空
a.clear()
4.获取全部kay
a.keys()
5.len(a)
"""
# a = {"小明":99,"小红":76,"小金":56}
# a['小明'] = 88
# print(a)
# a['小周'] = 100
# print(a)
# b = a.pop('小周')
# print(b)
# print(a)
# print(a.keys())
# #遍历字典 不支持下标索引，所以不可用while循环
# for i in a.keys():
#     print(i,end=' ')
#     print(a[i])

# #字典练习 级别大于一的工资加1000
# a = {'小明':{'部门':'科技部','工资':3000,'级别':1},
#      '小红':{'部门':'市场部','工资':5000,'级别':2},
#      '小周':{'部门':'市场部','工资':7000,'级别':3},
#      '小刚':{'部门':'科技部','工资':4000,'级别':1},
#      '小刘':{'部门':'市场部','工资':6000,'级别':2}}
# for i in a.keys():
#     if a[i]['级别']>1:
#         a[i]['工资']+=1000
# print(a)

# 容器的排序
a = [1,3,4,5,2,9,6,7]
b = sorted(a,reverse=True)
c = sorted(a)
print(a)
print(b)
print(c)
