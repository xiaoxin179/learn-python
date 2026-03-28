from ast import main
import spinder
import threading
import time
def single():
    for uri in spinder.url:
        spinder.craw(uri)
def thread():
    threads=[]
    for uri in spinder.url:
        t=threading.Thread(target=spinder.craw,args=(uri,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    start=time.time()
    #single()
    end=time.time()
    print(f"单线程爬虫时间：{end-start}秒")
    start=time.time()
    thread()
    end=time.time()
    print(f"多线程爬虫时间：{end-start}秒")
