from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = 'F:/360Downloads/Anaconda3/python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,1,3,4,5,5,4,1,3,9,9,10])
#去重
rdd1=rdd.distinct().collect()
print(rdd1)