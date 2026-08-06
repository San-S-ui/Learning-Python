
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
)

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql
cursor.execute("create table student(id int,name varchar(10) ,age int ,gender varchar(10) )")
# 关闭链接
conn.close()

