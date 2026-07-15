#导入包的方式一
import my_package.model1
import my_package.model2
my_package.model2.test2()
my_package.model1.test()
#导入包的方式二
from  my_package import model1
from my_package import model2
model1.test()
model2.test2()
#导入包的方式三
from my_package.model1 import test
from my_package.model2 import test2
test()
test2()
# all控制* 在init.py里