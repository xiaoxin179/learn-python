import queue
import spinder
import threading
import time
import random
# 消费url_queue 生成html_queue
def producer(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url=url_queue.get()
        html=spinder.craw(url)
        print("生产者生产了",f"线程的名称为：{threading.current_thread().name}",f"url队列的长度为：{url_queue.qsize()}")
        html_queue.put(html)
        time.sleep(random.randint(1,2))
def consumer(html_queue:queue.Queue,fout):
    while True:
        html=html_queue.get()
        result=spinder.parse(html)
        print("消费者消费了",f"线程的名称为：{threading.current_thread().name}",f"html队列的长度为：{html_queue.qsize()}")
        fout.write(str(result) + "\n")
        time.sleep(random.randint(1,2))
if __name__ == "__main__":
    url_queue=queue.Queue()
    html_queue=queue.Queue()
    for uri in spinder.url:
        url_queue.put(uri)
    for i in range(3):
        t=threading.Thread(target=producer,args=(url_queue,html_queue))
        t.start()   #t.start()不会阻塞后续进程的使用
    fout=open("html.txt","w")
    for i in range(2):
        t=threading.Thread(target=consumer,args=(html_queue,fout))
        t.start()
    

    