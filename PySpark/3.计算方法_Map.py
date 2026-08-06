from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON'] ='F:/360Downloads/Anaconda3/python.exe'

conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

#准备一个rdd
rdd = sc.parallelize([1,2,3,4,5])

#map 传入 lambda
rdd2 = rdd.map(lambda data: data * 10).map(lambda x:x+5)
#(T)->U 传入T返回U
print(rdd2.collect())
