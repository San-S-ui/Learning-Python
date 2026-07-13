a = 'Hello','LWL'
b = 'Hello''LWL'	
#注意字串符a与b的区别，如果有逗号，
#那么输出时将会是两个字串符一起输出，如
#果没有输出将会两个字串符相互结合输出

c,d= 'Hello','LWL'
print(a)#(Hello,LWL)
print(b)#HelloLWL
print(c,d)#Hello LWL
print(c+d)#HelloLWL
print(b[0:-2])#HelloL
print(c[0:-3])#He
print(d[0:-1])#LW
print(c*2,d*2)#各输出两次 HelloHello LWLLWL
print((c+d)*2)#结合输出两次HelloLWLHelloLWL
print('Hello,\nLWL')
print(r'Hello,\nLWL')#加了r后转义字符失效
e='Love LWL 1314'
print(e[0],e[5])#输出指定索引位置的字母
print(e[0],e[-2],e[3])#Python与C语言字串符不同的地方在于Python字串符是不可以被改变的，
                      #如果向一个指定索引赋值，那么将会错误
print('hello\tworld') # \t制表空格
print('I\'m LWL')     # \' 输出单引号
print("hello\\world") # \\输出反斜杠
print('He said, \"Hello!\"')#输出双引号
#不能直接修改指定索引字符，只能重新生成字符串
a = 'abc'
b ='x'+a[1:]
print(b)
#字符串没法通过加号与整数拼接所以需要字符串的格式化
# %占位符 s将变量变成字符串放入占位的地方 数字变为字符串
c =123
print('%s%s'%(a,c))
#%d 变为整数  %f 变为浮点数
print('*********************************************************************')
# 字符串的格式化 m宽度（%5d）  .n控制小数点的精度，四舍五入(%5.2f)
a =123.756
print ('%5d' %a)
print ('%9.2f' %a)
#快速格式化 f"内容{变量}" 无精度限制
print(f'数字{a}')
#表达式格式化 1+1  a=123 b = "张三"
print(f'数字{2*2}')
print('数字%.2f'%(a*a))
print("---------------------------------------------------------------------")
s='Python'
print(s[-3::-1])
print(s[3])
print(s[1:4])
print(s[::2])#[开始（从0）:结束（不包含）:步长（包含）]
print(s[::-1])
s = "hello Python"
print(s.upper())
print(s.lower())
print(s.split())
print(s.split("l"))
print(len(s))
print("P" in s)#s中是否有P
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#计算经过days天的增长后股价达到了多少天
name ="河南农业大学"
price = 20
code = 13245
factor = 1.2
days = 30
print (f'公司：{name},股票代码：{code},当前股价：{price},增长系数：%.1f,在%s天的增长后达到%.1f'%(factor,days,price+factor*days))
print('================================================================================')
#数据输入 input (字符串类型) 输出print
print("输入")
name = input()
print("名字：%s"%name)