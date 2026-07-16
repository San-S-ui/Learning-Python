def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r',encoding='utf-8')
        context = f.read()
        print(f"文件内容为：{context}")
    except:
        print("文件不存在")
    finally:
        if f!=None:
            f.close()
def append_to_file(file_name,data):
        f = open(file_name, 'a',encoding='utf-8')
        f.write(data)
        f.write('\n')
        f.close()
if __name__ == '__main__':
    print_file_info('test.txt')
    append_to_file('test.txt', 'Hello, World!')