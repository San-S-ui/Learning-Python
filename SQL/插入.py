from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
    autocommit=True     # 设置自动提交 
)

# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
cursor.execute("insert into student  values(10002, '林俊节', 31, '男')")
#手动提交
# conn.commit()
conn.close()