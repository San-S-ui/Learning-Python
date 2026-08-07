import socket
socket_client=socket.socket()
socket_client.connect(('localhost',8888))
while True:
    msg = input('输入要发送的信息：')
    if msg=='exit':
        break
    socket_client.send(msg.encode('UTF-8'))
    #接收返回的消息
    data=socket_client.recv(1024)
    print(f"服务端回复的消息是：{data.decode('UTF-8')}")
socket_client.close()