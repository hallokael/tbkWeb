'''
Created by auto_sdk on 2016.05.10
'''
from top.api.base import RestApi
class AlibabaBaichuanAppRecommendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appid = None
		self.bizid = None
		self.params = None

	def getapiname(self):
		return 'alibaba.baichuan.app.recommend'
