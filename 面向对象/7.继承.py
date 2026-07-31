'''
class 类名（父类）：
    ......
子类不可以直接访问父类的私有成员
'''
class Phone:
    name = 'iphone 12'
    def fuc1(self):
        print('5G')
class iphone(Phone):
    #新功能
    def fuc2(self):
        name = 'iphone 13'
        print(f'name:{name},6G')
    def fuc3(self):
        name = 'iphone 13'
        print(f'name:{self.name},6G')#先看子类有没有name,没有再去父类找iphone 12
x = iphone()
x.fuc2()
x.fuc3()

# 演示多继承
class NFCReader:
    name = 'iphone 14'
    nfc_type = "第五代"
    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    name = 'iphone 15'
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")
class MyPhone(Phone,NFCReader,RemoteControl):
    #继承了别的类又不想补充其他功能了
    pass
phone = MyPhone()
phone.read_card()
phone.write_card()
phone.control()
print(phone.name)#(Phone,NFCReader,RemoteControl):先继承谁谁优先


