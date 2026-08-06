from pyspark import SparkContext, SparkConf
import os
import json
os.environ['PYSPARK_PYTHON'] = 'F:/360Downloads/Anaconda3/python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1. 读取数据文件
rdd = sc.textFile(r"D:\pythonProject2\Learning\PySpark\data\orders.txt")
str_rdd=rdd.flatMap(lambda x:x.split('|'))
# print(str_rdd.collect())

# 需求1：城市销售额排名
#先转为字典
dict_rdd=str_rdd.map(lambda x:json.loads(x))
# print(dict_rdd.collect())
# 取出城市和销售额数据
# (城市，销售额)
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b)
#按销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1的结果：", result1_rdd.collect())


# 需求2：全部城市有哪些商品类别在售卖
# 取出全部的商品类别
category_rdd = dict_rdd.map(lambda x: x['category']).distinct()
print("需求2的结果：", category_rdd.collect())
# 对全部商品类别进行去重


# # 需求3： 北京市有哪些商品类别在售卖
# # 过滤北京市的数据
# beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')
# # 取出全部商品类别
# result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()
# print("需求3的结果：", result3_rdd.collect())
