'''
文件相关的类
'''
from data_define import Record
import json
class File_reader:
    def read_data(self)->list[Record]:
    #读到的数据转换为Record对象，将他们封装到 List
        pass
class Text_Reader(File_reader):
    def __init__(self,path):
        self.path = path #记录文件路径 构建类对象时就记录了路径

    #实现抽象方法(text文件)
    def read_data(self)->list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list=[]
        for line in f.readlines():
            #消除空行
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])#record是'2011-02-23, 9e135b5e-dfad-46fa-a300-b508f9aaaa89, 136, 广西省'类型  本质是字符串
            record_list.append(record)
        # print(record_list)
        f.close()
        return record_list
    #实现抽象方法(json文件)
class JSON_Reader(File_reader):
    def __init__(self,path):
        self.path = path #记录文件路径 构建类对象时就记录了路径
    def read_data(self)->list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list=[]
        for line in f.readlines():
            #将json转为字典
            data_dict=json.loads(line)
            record = Record(data_dict['date'],data_dict['order_id'],data_dict['money'],data_dict['province'])
            record_list.append(record)
        # print(record_list)
        f.close()
        return record_list
            # print(data_dict)
            
if __name__=='__main__':
    text = Text_Reader(r'D:\pythonProject2\Learning\数据分析案例\data\2011年1月销售数据.txt')
    list1 = text.read_data()
    json1 = JSON_Reader(r'D:\pythonProject2\Learning\数据分析案例\data\2011年2月销售数据JSON.txt')
    list2 = json1.read_data()
    for i in list1:
        print(i,type(i))
    for i in list2:
        print(i,type(i))