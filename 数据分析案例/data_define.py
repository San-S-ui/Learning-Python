'''
定义数据的类
Record数据类型
'''
class Record:
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.id = order_id
        self.money = money
        self.province = province
    def __str__(self):
        #返回的是字符串   例如'2011-01-02, 8f1b483d-4aa6-45d8-bb80-17759bc42d41, 2346, 安徽省'
        return f"{self.date}, {self.id}, {self.money}, {self.province}"

    def __repr__(self):
        #返回的是字符串   例如'2011-01-02, 8f1b483d-4aa6-45d8-bb80-17759bc42d41, 2346, 安徽省'
        return f"{self.date}, {self.id}, {self.money}, {self.province}"
        