#Animal为抽象类，因为它含有抽象方法speak 函数体为pass的方法（没有具体实现）为抽象方法,也可以叫做接口
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print('汪汪汪')
class Cat(Animal):
    def speak(self):
        print('喵喵喵')
#同一行为不同的状态
def make_noice(animal:Animal)->str:
    animal.speak()
anm1 = Dog()
make_noice(anm1)
anm2 = Cat()
make_noice(anm2)