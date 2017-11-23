'''
Created by auto_sdk on 2016.09.28
'''
from top.api.base import RestApi
class OpenAccountIndexFindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.index_type = None
		self.index_value = None

	def getapiname(self):
		return 'taobao.open.account.index.find'
