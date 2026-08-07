import socket
#创建对象
socket_server = socket.socket()
#绑定ip和端口
socket_server.bind(('localhost',8888))
#监听端口,参数是监听的端口数
socket_server.listen(1)
#等待连接
#返回连接对象和地址信息
conn,address=socket_server.accept()#accept返回的是元组
print(f'我找到了客户端的连接，客户端地址信息是{address}')
while True:
    #接受客户端信息 decode():bytes → str字符串
    data:str=conn.recv(1024).decode('UTF-8')
    # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    print(f'客户端发来的消息是：{data}')
    msg = input("输入你要回复客户端的信息：")
    if msg=='exit':
        break
    # encode():str → bytes 字节
    conn.send(msg.encode('UTF-8'))
#关闭连接
conn.close()
socket_server.close()