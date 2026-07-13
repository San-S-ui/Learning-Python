"""
1.打开文件
open(name,mode,encoding)
r 只读
w 写入（已存在则覆盖写）
a 追加（在文件末尾写）
2.读取
3关闭
"""
# 打开 得到文件f对象
# f = open('D:\pythonProject2\Learning\测试','r',encoding='UTF-8')
# 读取 read(字节数)  readlines() 读取全部行 readline()一次读一行
# 读文件是有指针的会续接上次读的位置
# a= f.read(8)
# print(a)
# print('-----------------------')
# b = f.readlines()
# print(b)
# c = f.readline()
# print(c)
#关闭
# f.close()
# with open() as f: 可以自动close
# with open('D:\pythonProject2\Learning\测试','r',encoding='UTF-8') as f:
#     for line in f:
#         print(line)

#统计字符
# with open('D:\pythonProject2\Learning\word','r',encoding='UTF-8') as f:
#     count = 0
#     for i in f:
#         a = i.split(" ")
#         print(a)
#         for j in a:
#             j = j.strip()
#             print(j)
#             if j =='itheima':
#                 count+=1
#     print(count)

# with open('D:\pythonProject2\Learning\word','r',encoding='UTF-8') as f:
#     i = f.read()
#     count =i.count('itheima')
#     print(count)

'''
文件的写入
f.write 在内存中
f.flush 写入硬盘
'''
# f = open(r'D:\pythonProject2\Learning\new','w',encoding='UTF-8')
# f.write('Hello World')
# f.flush()
# f.close() #close内置了flush
# f = open(r'D:\pythonProject2\Learning\new','w',encoding='UTF-8')
# f.write('12345')
# f.close()

#追加
# f = open(r'D:\pythonProject2\Learning\new','a',encoding='UTF-8')
# f.write("qwe\naqe")
# f.close()

#备份练习
