import threading
import time

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)
def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    th1 = threading.Thread(target=sing,args=('唱歌123',))
    th2 = threading.Thread(target=dance,kwargs={'msg':'跳舞456'})
    th1.start()
    th2.start()