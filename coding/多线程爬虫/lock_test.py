import threading
import time
lock=threading.Lock()
class Accout:
    def __init__(self,balance):
        self.banlance=balance 
def getMoney(accout:Accout,money):
    with lock:
        if accout.banlance >= money:
            time.sleep(0.1) # sleep 模拟网络延迟，sleep一定是阻塞的
            print(f"取钱成功，线程为{threading.current_thread().name}")
            accout.banlance -= money
            print(f"现在的余额为：{accout.banlance}")
        else:
            print("余额不足")

if __name__ == "__main__":
    accout=Accout(1000)
    
    t1=threading.Thread(target=getMoney,args=(accout,700),name="t1")
    t2=threading.Thread(target=getMoney,args=(accout,700),name="t2")
    t1.start()
    t2.start()