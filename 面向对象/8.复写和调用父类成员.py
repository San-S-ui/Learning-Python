'''
复写的同时调用父类方法：
1.父类名.
2.super
'''
class Phone:
    produce = 'iphone 13'
    def func(self):
        print('父类方法')
class myphone(Phone):
    produce  = 'iphone 14'
    #复写父类成员
    def func(self):
        print('子类方法')
        # #方法1：
        # #复写的同时调用父类成员：
        # print(f'父类产品：{Phone.produce}')
        # #复写的同时调用父类方法：
        # Phone.func(self)
        #方法2：
        #复写的同时调用父类成员：
        print(f'父类产品：{super().produce}')
        #复写的同时调用父类方法：
        super().func()
phone = myphone()
print(f"调用子类对象:{phone.produce}")
phone.func()