import requests
from lxml import etree

url      = "https://movie.douban.com/top250"
headers  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res      = requests.get(url, headers=headers)
html_str = res.text
root     = etree.HTML(html_str)

items = root.xpath("//div[@class='hd']")
for item in items:
	i_name = item.xpath("./a/span[1]/text()")[0]
	i_url  = item.xpath("./a/@href")[0]
	print(i_name, ': ', i_url, sep='')