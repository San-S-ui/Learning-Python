#自定义模块
#如果两个模块有同名函数，会默认执行下面的那个
#不想用模块中的测试 要在if __name__ == '__main__':下写测试
from My_Model import *
func(1,2)
#*作用到all,all设为只是func()了
func2(1,4)

from my_package import *
model1.test()
#无法用model2


