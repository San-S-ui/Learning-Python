#封装对用户隐藏属性和行为,不对外开放
#私有成员类对象无法使用 可以被类中其他对象使用
class Phone:
    #私有成员变量
    __volt = 9
    #私有方法
    def __fun1(self):
        print('手机运行')
    def fun2(self):
        if self.__volt >10:
            print('符合')
        else:
            self.__fun1()
            print('不符合')
    
stu = Phone()
stu.fun2()