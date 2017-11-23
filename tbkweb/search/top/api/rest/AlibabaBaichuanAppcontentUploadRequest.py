'''
Created by auto_sdk on 2016.05.10
'''
from top.api.base import RestApi
class AlibabaBaichuanAppcontentUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appid = None
		self.bizid = None
		self.operate = None
		self.params = None

	def getapiname(self):
		return 'alibaba.baichuan.appcontent.upload'
