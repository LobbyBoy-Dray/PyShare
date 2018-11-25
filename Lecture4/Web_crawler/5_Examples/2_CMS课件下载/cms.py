import requests
import os
from lxml import etree


class CmsSpider:
	def __init__(self, documentUrl, account, password, dirName):
		self.loginUrl = "http://cms.phbs.pku.edu.cn/claroline/auth/login.php"
		self.documentUrl = documentUrl
		self.headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.9',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'cms.phbs.pku.edu.cn',
			'Origin': 'http://cms.phbs.pku.edu.cn',
			'Proxy-Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
		}
		self.data = {
			'login':account,
			'password':password,
			'submitAuth': 'Enter',
		}
		self.savePath = dirName
		self.session  = None

	def getSession(self):
		return self.session

	def setSession(self, session):
		self.session = session

	# 登录操作
	def login(self):
		s = requests.Session()
		s.post(self.loginUrl, headers = self.headers, data = self.data)
		self.setSession(s) 

	# 根据document页面的html获取所有file的url
	def getFileUrl(self, text):
		root  = etree.HTML(text)
		urls  = root.xpath("//a[@class=' item']/@href")
		urls  = ["http://cms.phbs.pku.edu.cn"+url for url in urls]
		temp  = root.xpath("//a[@class=' item']")
		names = [each.xpath("string(.)").strip() for each in temp]
		return names, urls

	# 下载所有文件
	def downloadAllFiles(self, session, savePath, fileNames, fileUrls):
		for name, url in zip(fileNames, fileUrls):
			r = session.get(url, headers = self.headers)
			content = r.content
			filePath = os.path.join(self.savePath, name)
			with open(filePath, 'wb') as f:
				f.write(content)
			print("下载完毕：【%s】" % name)			


	def main(self):
		# 登录
		self.login()
		s = self.getSession()
		# 获取document页面的html
		r = s.get(self.documentUrl, headers = self.headers)
		text = r.text
		# 判断存储文件夹是否存在，不存在则创建
		if not os.path.exists(self.savePath):
			os.mkdir(self.savePath)
		# 获取文件名及文件url
		fileNames, fileUrls = self.getFileUrl(text)
		# 下载所有文件
		self.downloadAllFiles(s, self.savePath, fileNames, fileUrls)


if __name__ == '__main__':
	dirName     = ""
	documentUrl = ""
	account     = ""
	password    = ""
	mySpider    = CmsSpider(documentUrl, account, password, dirName)
	mySpider.main()
