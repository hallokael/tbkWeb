'''
Created by auto_sdk on 2016.11.18
'''
from top.api.base import RestApi
class OpenAccountTokenValidateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_token = None

	def getapiname(self):
		return 'taobao.open.account.token.validate'
