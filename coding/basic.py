import cmath
import time
class test:
    # self的本质是调用实例对象的本身
    def testcase(self) -> None:
        print(dir(cmath))
    def testime(self):
        start=time.perf_counter()
        print(time.localtime(time.time()))
        print(time.asctime(time.localtime(time.time())))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        end = time.perf_counter()
        print(time.time)
        print("消耗的总的时间为："+str((end-start)*1000)+"ms")
class calucator:
    def __init__(self):
        self.result=0
        self.money=12  #定义其中的私有变量
if __name__ == '__main__':
    t=test()
    t.testime()
    calutor=calucator()
    print(calutor.money)
