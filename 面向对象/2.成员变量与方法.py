'''
类里面的函数为方法
方法要想访问成员变量就要用到self
self在传参时可以忽略掉
'''
class Student:
    name = None
    #self必须要写
    def say(self):
        print(f'大家好，我是{self.name}')
    def say1(self,x):
        print(f'大家好，我是{self.name},{x}')

stu1 = Student()
stu1.name= '张三'
stu1.say()
stu1.say1('在这')