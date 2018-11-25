import requests 			# 需要conda install requests以安装requests库
import pymongo 				# 需要conda install pymongo以安装pymongo库
import time
import re
from lxml import etree


class KindleSpider:
	def __init__(self, goodName, goodID, pageTotal):
		self.goodName  = goodName
		self.goodID    = goodID
		self.pageTotal = pageTotal
		self.headers   = {
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"zh-CN,zh;q=0.9",
			"Cache-Control":"max-age=0",
			"Connection":"keep-alive",
			"Host":"www.amazon.cn",
			"Upgrade-Insecure-Requests":"1",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
		}
		self.host = "127.0.0.1"
		self.port = 27017
		self.db   = "Amazon"
		self.coll = "good-review"
		
	# 下载一页，返回响应对象
	def crawlOnePage(self, pageNum):
		goodUrl = "https://www.amazon.cn/%s/product-reviews/%s/ref=cm_cr_getr_d_paging_btm_%s?ie=UTF8&reviewerType=all_reviews&pageNumber=%s" % (self.goodName, self.goodID, pageNum, pageNum)
		r = requests.get(goodUrl, headers = self.headers)
		return r

	# 传入单页的html内容，解析，返回由10条评论信息组成的列表
	def getInfo(self, text):
		info  = []
		root  = etree.HTML(text)
		items = root.xpath("//div[@data-hook='review']")
		for item in items:
			# 用户名
			username = item.xpath("./div[1]/div[1]//span[@class='a-profile-name']/text()")[0]
			# 星星数
			star     = item.xpath("./div[1]/div[2]//i[@data-hook='review-star-rating']/span/text()")[0]
			pattern = re.compile(r"\d\.\d")
			star = float(pattern.search(star).group())
			# 标题
			title    = item.xpath("./div[1]/div[2]/a[@data-hook='review-title']/text()")[0]
			# 发布日期
			reviewdate = item.xpath("./div[1]/span[@data-hook='review-date']/text()")[0]
			# 内容
			content  = item.xpath("./div[1]/div[4]/span[@data-hook='review-body']")[0]
			content  = content.xpath("string(.)")
			info.append({"username":username, "star":star, "title":title, "reviewdate":reviewdate, "content":content})
		return info

	# 传入包含10个评论信息的列表，一次性向mongodb中插入
	def insertToMongoDB(self, info):
		client = pymongo.MongoClient(host = self.host, port = self.port)
		db     = client[self.db]
		coll   = db[self.coll]
		coll.insert(info)

	def main(self):
		for i in range(pageTotal):
			pageNum = i+1
			r = self.crawlOnePage(pageNum)
			pageInfo = self.getInfo(r.text)
			self.insertToMongoDB(pageInfo)
			print("第%s页完成" % str(pageNum))
			time.sleep(0.8)


if __name__ == '__main__':
	goodName = "Kindle-Paperwhite电子书阅读器-300-ppi超清电子墨水触控屏-内置阅读灯-超长续航"			# 商品名称
	goodID = "B017DOUQOK"																	# 商品ID
	pageTotal = 1938																		# 评论总页数
	kSpider = KindleSpider(goodName, goodID, pageTotal)
	kSpider.main()




