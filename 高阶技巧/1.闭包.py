#闭包即函数嵌套。其中要想修改外部函数的值要用nonlocal修饰
def create_account(init_account = 0):
    def atm(num,flag = True):
        nonlocal init_account
        if flag:
            init_account+=num
            print(f'存入后余额为{init_account}')
        else:
            init_account-=num
            print(f'取款后余额为{init_account}')
    return atm
fn = create_account()
fn(100)
fn(50,False)
