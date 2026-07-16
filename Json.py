"""
json的格式
{“key”:”value”，”key”:”value”}
[{""key":”value”，”key”:”value”}]
"""

import json
data = [{"name": "张三", "age": 25}, {"name": "李四", "age": 30},{"name": "王五", "age": 28}]
json_str=json.dumps(data, ensure_ascii=False)  # 将Python对象转换为JSON字符串，并保持中文字符不转义
print(type(json_str))  # 输出：<class 'str'>
print(json_str)  # 输出JSON字符串
json_data = json.loads(json_str)  # 将JSON字符串转换为Python对象
print(type(json_data))  # 输出：<class 'list'>
print(json_data)  # 输出Python对象
print('-------------------')
d = {'name': '张三', 'age': 25, 'city': '北京'}
print(json.dumps(d, ensure_ascii=False))  # 输出：{"name": "张三", "age": 25, "city": "北京"}
print(type(d))#d 还是字典
print('-------------------')
da = '[{"name": "张三", "age": 25}, {"name": "李四", "age": 30},{"name": "王五", "age": 28}]'
print(type(da))#da 是字符串
da1 = json.loads(da)  # 将JSON字符串转换为Python对象
print(type(da1))  # 输出：<class 'list'>