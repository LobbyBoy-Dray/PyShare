import requests
import pymongo 
import time
import re
from lxml import etree



class ZHSpider:
	def __init__(self, topic_id, each_page=10):
		self.topic_id  = topic_id
		self.topic_title = "暂未获取"
		self.each_page = each_page	# 不能再多了
		self.host = "127.0.0.1"
		self.port = 27017
		self.db   = "ZhiHu"
		self.coll = "topic"
		self.headers = {
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"accept-language":"zh-CN,zh;q=0.9",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
		}

	def insertToMongoDB(self, info):
		client = pymongo.MongoClient(host = self.host, port = self.port)
		db     = client[self.db]
		coll   = db[self.coll]
		coll.insert(info)

	def removeHtml(self, html):
		dr = re.compile(r'<[^>]+>', re.S)
		dd = dr.sub('', html)
		return dd

	def getTopicTitle(self):
		url   = "https://www.zhihu.com/topic/%d/hot" % self.topic_id
		r     = requests.get(url, headers = self.headers)
		root  = etree.HTML(r.text)
		title = root.xpath("//*[@class='TopicMetaCard-title' or @class='TopicCard-titleText']/text()")[0].strip()
		self.topic_title = title

	def getPageContent(self, url):
		r     = requests.get(url, headers = self.headers)
		data  = r.json()
		items = data["data"]
		info  = []
		for item in items:
			isQuestion = item["target"].get("question")
			if not isQuestion:
				continue
			topic_id        = self.topic_id
			topic_title     = self.topic_title
			question_id     = item["target"]["question"]["id"]
			question_title  = item["target"]["question"]["title"]
			answer_id       = item["target"]["id"]
			answer_content  = item["target"]["content"]
			answer_content  = self.removeHtml(answer_content)
			answer_len      = len(answer_content)
			answer_vote     = item["target"]["voteup_count"]
			anthor_id       = item["target"]["author"]["id"]       # 用户id
			anthor_gender   = item["target"]["author"]["gender"]   # 性别
			anthor_name     = item["target"]["author"]["name"]     # 用户名
			anthor_headline = item["target"]["author"]["headline"] # 用户slogan
			temp = {}
			temp["topic_id"]        = topic_id
			temp["topic_title"]     = topic_title
			temp["question_id"]     = question_id
			temp["question_title"]  = question_title
			temp["answer_id"]       = answer_id
			temp["answer_content"]  = answer_content
			temp["answer_len"]      = answer_len
			temp["answer_vote"]     = answer_vote
			temp["anthor_id"]       = anthor_id
			temp["anthor_gender"]   = anthor_gender
			temp["anthor_name"]     = anthor_name
			temp["anthor_headline"] = anthor_headline
			info.append(temp)
		is_end    = data["paging"]["is_end"]
		next_page = data["paging"]["next"]
		return info, is_end, next_page

	def main(self):
		self.getTopicTitle()
		print("*******%s--%d*******" % (self.topic_title, self.topic_id))
		url     = "https://www.zhihu.com/api/v4/topics/%d/feeds/essence?include=data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;&limit=%d" % (self.topic_id, self.each_page)
		is_end  = False
		counter = 0
		while True:
			info, is_end, next_page = self.getPageContent(url)
			if is_end:break
			if info:self.insertToMongoDB(info)
			counter += 1
			print("第%d页! url: %s" % (counter, url))
			url = next_page
			# time.sleep(2)


if __name__ == '__main__':
	topic_ids = [19646208, 19631190, 19552234]
	for topic_id in topic_ids:
		mySpider = ZHSpider(topic_id)
		mySpider.main()

