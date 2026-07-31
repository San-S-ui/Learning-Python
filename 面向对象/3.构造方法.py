#__init__方法，称为构造方法（魔术方法之一） 构建类对象是会自动执行，将传入参数自动传递给init方法使用

class Student:
    #这三行可以省略
    name = None
    age = None
    tel = None
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('创建类了对象')

stu = Student('张三',12,'13888888888')#这时就自动运行init了
print(stu.name,stu.age,stu.tel)