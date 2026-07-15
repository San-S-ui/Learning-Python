# #定义一个函数计算字符串方的长度
# #无返回值是None None=False
# def jisuan(data):
#     count=0
#     for i in data:
#         count+=1
#     print(count)
# jisuan('1234')
# print(jisuan('1234'))
# #传入参数   两个数字相加
# def jia(x,y):
#     '''
#     :param x: 数字一
#     :param y: 数字二
#     :return: 两数相加
#     '''
#     return x+y
# print(jia(1,5))

# def age(age):
#     if age>18:
#         return 'success'
# a = age(12)
# print(a)

# #嵌套调用
# def func1():
#     return 1
# def func2():
#     a = func1()
#     return 3,a
# print(func2())

# #局部变量与全局变量 局部变量在执行完函数后会被销毁
# def func():
#     a = 1
#     print(a)
# func()
# # print(a)

# #global 关键字 函数内声明全局变量
# num = 200
# def func ():
#     global num
#     num = 100
#     print(num)
# func()
# print(num)

# #ATM取款
# money = 1000000
# name = None
# def yuechaxun():
#     global money
#     print(f'您的余额是{money}')
# def qukaun(x):
#     '''
#     :param x:取得钱数
#     :return: 剩下的
#     '''
#     global money
#     money = money-x
#     if money>0:
#         print(f"还剩余{money}元")
#     else:
#         print('没钱了')
# def cunkaun(x):
#     '''
#     :param x:存的钱
#     :return: 剩下的
#     '''
#     global money
#     money = money+x
#     print(f"还剩余{money}元")
# print('请输入姓名')
# name = input()
# print('---------主菜单---------')
# print(f'{name},欢迎使用ATM。请选择操作：')
# print('余额查询 [输入1]')
# print('存款 [输入2]')
# print('取款 [输入3]')
# print('退出 [输入4]')
# flag =True
# while flag:
#     print('请输入你的选择')
#     a = int(input())  # a记录用户选择
#     if a==1:
#         print('---------余额---------')
#         yuechaxun()
#     elif a==2:
#         print('---------取款---------')
#         print('输出入取款金额')
#         b = int(input())
#         qukaun(b)
#     elif a==3:
#         print('---------存款---------')
#         print('输出入存款金额')
#         c = int(input())
#         cunkaun(c)
#     else:
#         print('程序退出')
#         break

'''
函数拓展
'''
# #多返回值
# def func():
#     return 1,2
# a,b= func()
# print(func())
# print(a)
# print(b)

#传参方式
#
"""
a(x,y)
位置传参 a(1,2)
关键字传参a(x=1,y=2)
可以混用  位置在前，关键字在后
缺省参数
func(x,y=1)默认的必须再最后
func(2)
func(1,3)传了默认的会被覆盖
可变参数
位置传递
"""
# #位置传递 元组
# def func (*args):
#     print(args)
# func(1)
# func('as','sd')

# #关键字传递 参数是键值对 字典
# def fun(**kwargs):
#     print(kwargs)
# fun(name='as',age='qw')

# 综合示例：打印用户信息
def print_user_info(*args, **kwargs):
    """
    打印用户信息，结合*args和**kwargs
    :param args: 爱好列表（可变位置参数）
    :param kwargs: 用户基本信息（可变关键字参数）
    """
    print("===== 用户信息 =====")
    # 打印基本信息（来自kwargs）
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # 打印爱好（来自args）
    if args:
        print("爱好:", ", ".join(args))
    print("===================")

# 调用示例
print_user_info("篮球", "音乐", "编程", name="小明", age=25, city="北京")

