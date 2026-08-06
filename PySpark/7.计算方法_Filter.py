#进行数据过滤，true保留，false不保留
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = 'F:/360Downloads/Anaconda3/python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#偶数保留奇数过滤
rdd = sc.parallelize([1,2,3,4,5])
rdd1 = rdd.filter(lambda x:x%2==0).collect()
print(rdd1)