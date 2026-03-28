import queue
import spinder
import threading
import time
import random
# 生产者：从 url_queue 取 URL，爬取页面后放入 html_queue
def producer(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url=url_queue.get()
        html=spinder.craw(url)
        print("生产者生产了",f"线程的名称为：{threading.current_thread().name}",f"url队列的长度为：{url_queue.qsize()}")
        html_queue.put(html)
        time.sleep(random.randint(1,2))
# 消费者：从 html_queue 取页面内容，解析后写入文件
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
    # 启动3个生产者线程
    # 注意：t.start() 不会等待线程执行完毕，它只是"启动"线程然后立刻返回
    # 所以这里3个 for 循环创建完3个线程后，主线程会立刻继续往下走
    # 3个 producer 线程会同时并发执行，不断从 url_queue 取 URL 并爬取页面
    for i in range(3):
        t=threading.Thread(target=producer,args=(url_queue,html_queue))
        t.start()

    fout=open("html.txt","w")

    # 启动2个消费者线程
    # 由于 t.start() 不会阻塞，即使生产者线程可能还没开始执行（或还在爬取），
    # 主线程也会立刻启动消费者线程。消费者线程会等待 html_queue 中有数据后开始消费
    for i in range(2):
        t=threading.Thread(target=consumer,args=(html_queue,fout))
        t.start()
    

    