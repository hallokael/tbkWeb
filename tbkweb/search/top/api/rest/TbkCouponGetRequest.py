'''
Created by auto_sdk on 2017.08.25
'''
from top.api.base import RestApi
class TbkCouponGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.me = None

	def getapiname(self):
		return 'taobao.tbk.coupon.get'
