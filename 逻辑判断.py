# == ,!=,>,<,>=,<= 结果是bool类型
a = 1
b = 2
print(a==b)
# print('输入数字a')
# a=int(input())
# print('输入数字b')
# b=int(input())
# if a<b:
#     print('b大')
# elif a>b:
#     print("a大")
# else:
#     print("a等于b")

#判断语句嵌套  猜数字游戏
# import random
# num = random.randint(1,10)
# print("请猜一个数字（1-10）")
# guess = int(input())
# if num ==guess:
#     print("猜中了")
# elif (num>guess):
#         print("猜小了 再猜一次")
#         guess = int(input())
#         if(num ==guess):
#             print("猜中了")
#         elif(num>guess):
#             print("猜小了 再猜一次")
#             guess = int(input())
#             if (num == guess):
#                 print("猜中了")
#             else:
#                 print("没机会了，正确答案是%d" % num)
#         elif (num < guess):
#             print("猜大了 再猜一次")
#             guess = int(input())
#             if (num == guess):
#                 print("猜中了")
#             else:
#                 print("没机会了，正确答案是%d"%num)
# elif (num<guess):
#         print("猜大了 再猜一次")
#         guess = int(input())
#         if(num ==guess):
#             print("猜中了")
#         elif(num>guess):
#             print("猜小了 再猜一次")
#             guess = int(input())
#             if (num == guess):
#                 print("猜中了")
#             else:
#                 print("没机会了，正确答案是%d"%num)
#         elif (num < guess):
#             print("猜大了 再猜一次")
#             guess = int(input())
#             if (num == guess):
#                 print("猜中了")
#             else:
#                 print("没机会了，正确答案是%d"%num)

# while 计算1-100的和  python中没有i++
# i =1
# result = 0
# while(i<=100):
#     result +=i
#     i+=1
# print("1-100的和是%d"%result)

#while猜数字
# import random
# num = random.randint(1,10)
# print("输入你猜的数字")
# guess=int(input())
# count = 1
# while guess!=num:
#     count+=1
#     if(num>guess):
#         print("猜小了重新猜")
#         guess = int(input())
#     elif(num<guess):
#         print("猜大了重新猜")
#         guess = int(input())
# print("恭喜你猜中了，这个数是%d,一共猜了%d次"%(num,count))

#while嵌套  九九乘法表 print( ,end='') 不换行  \t制表符
# j = 1
# while(j<=9):
#     i=1
#     while(i<=j):
#         print('%d*%d=%d\t'%(i,j,i*j),end=' ')
#         i+=1
#     j+=1
#     print()

# for循环  for  in :
# name = "ashueaniaefafusasdea"
# count =0
# for x in name:
#     if x =="a":
#         count+=1
# print(count)
# print("----------------------------------------------------------")
# range语句 生成序列  range(num1,num2(不包含),step)
#100内有几个偶数

# num=101
# count = 0
# for x in range(100):
#     if(x%2==0):
#         count+=1
#         print(x,end=' ')
# print()
# print(count)
# print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#临时变量作用域只在逻辑语句内有用，但是不遵守也可以运行

# for i in range(4):
#     print(i)
# print(i)

#for循环九九乘法表

# for j in range(1,10):
#     for i in range(1,j+1):
#         print('%d*%d=%d\t'%(i,j,i*j),end='')
#     print()

#break和continue
#continue 结束本次循环直接进入下一次

# for i in range(4):
#     print('语句一')
#     for j in range(4):
#         print('语句二')
#         continue
#         print('语句三')
#     print("语句四")
# print('=========================================================')
#
# for i in range(4):
#     print('语句一')
#     for j in range(4):
#         print('语句二')
#         break
#         print('语句三')
#     print("语句四")

#发工资
import random
gongzi =10000
for i in range(20):
    if gongzi>0:
        jixiao = random.randint(1, 10)
         # 绩效低于5的不发工资
        if jixiao < 5:
            print(f"员工{i}，绩效是{jixiao},没领到工资")
            continue
        else:
            gongzi -= 1000
            print(f"员工{i}，绩效是{jixiao},领到了工资，工资还有{gongzi}")
    else:
        print("工资发完了")
        break

