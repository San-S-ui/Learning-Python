#一个类只有一个实例
from str_Tool import str_tool
s1 = str_tool
s2 = str_tool
print(id(s1))
print(id(s2))