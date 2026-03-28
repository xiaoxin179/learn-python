import requests
url=[
    f"https://www.cnblogs.com/#{page}"
    for page in range(1,51)
]
def craw(url):
    r=requests.get(url)
    print("爬取成功，url:"+url+"，长度："+str(len(r.text)))
craw(url[0])

