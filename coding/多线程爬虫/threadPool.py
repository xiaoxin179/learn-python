import threading
import concurrent.futures
import spinder

# 阶段1：并发爬取所有页面
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    htmls = pool.map(spinder.craw, spinder.url)
    htmls = list(zip(spinder.url, htmls))
    with open("html2.txt", "w", encoding="utf-8") as fount:
        fount.write(str(htmls))

# 阶段2：并发解析所有页面内容
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    futures = {}
    for url, html in htmls:
        futures[url] = pool.submit(spinder.parse, html)

    # 所有解析任务完成后，再写入文件
    with open("html3.txt", "w", encoding="utf-8") as fout:
        for url, future in futures.items():
            fout.write(str(future.result()) + "\n")
