# # 捕获异常
# #捕捉单个异常
# try:
#     f = open('不存在.txt','r',encoding='UTF-8')
# except:
#     print('文件不存在，异常，为你改用’w‘打开')
#     f = open('不存在.txt','w',encoding='UTF-8')
#
# #捕捉指定
# try:
#     1/0
# except ZeroDivisionError as a:
#     print("捕捉到ZeroDivisionError异常")
#     print(a)#异常信息
#
# # 捕获多个异常
# try :
#     1/0
# except (ZeroDivisionError,NotADirectoryError) as a:
#     print("异常")
# #捕获全部异常
# try:
#     1/0
# except Exception as a:
#     print('捕捉全部异常')
# #异常的else
# try:
#     f = open('不存在.txt', 'r', encoding='UTF-8')
# except:
#     print('文件不存在，异常，为你改用’w‘打开')
#     f = open('不存在.txt', 'w', encoding='UTF-8')
# else:
#     print('无异常')
#
# #finally 有没有异常都执行
# try:
#     f = open('不存在.txt', 'r', encoding='UTF-8')
# except:
#     print('文件不存在，异常，为你改用’w‘打开')
#     f = open('不存在.txt', 'w', encoding='UTF-8')
# else:
#     print('无异常')
# finally:
#     f.close()#有没有异常我都要关闭

#
# #异常的传递
# def func1():
#     a = 1/0
#     print("这是一个异常")
# def func2():
#     print("fun2函数")
#     func1()
#     print("fun2结果")
# def main():
#     try:
#         func2()
#     except Exception as b:
#         print(b)
# main()
