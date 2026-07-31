#构造方法就是魔术方法的一种，但魔术方法不仅仅只有构造方法

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #默认str是返回地址，这里重写了
    def __str__(self):
        return f'我是{self.name},{self.age}'#str返回类型必须是字符串
    #不可以比较两个对象，但在lt里可以实现
    def __lt__(self, other):
        return self.age<other.age
    #负责>=或者<=
    def __le__(self, other):
            return self.age<=other.age
    #负责==
    def __eq__(self, other):
                return self.age==other.age
stu1 = Student('张三',18)
stu2 = Student('张三',7)
stu3 = Student('张三',18)
print(stu1)
print(stu1<stu2)
print(stu1>stu2)#lt自动转换为stu2<stu1
print(stu1<=stu3)#le不负责等于
print(stu1==stu3)