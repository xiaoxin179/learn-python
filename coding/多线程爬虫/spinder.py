import requests
from bs4 import BeautifulSoup
# 改造思路:生产者解析网页，消费者存储为文件
url=[
    f"https://www.cnblogs.com/#{page}"
    for page in range(1,51)
]
def craw(url):
    request=requests.get(url)
    return request.text
# 解析html函数
def parse(html):
    soup=BeautifulSoup(html,"html.parser")
    links=soup.find_all("a",class_="post-item-title")
    return [(link["href"],link.get_text()) for link in links]

if __name__ == "__main__":
    print(parse(craw(url[0])))
