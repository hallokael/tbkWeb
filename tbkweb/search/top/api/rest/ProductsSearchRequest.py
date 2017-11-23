'''
Created by auto_sdk on 2015.04.21
'''
from top.api.base import RestApi
class ProductsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.barcode_str = None
		self.cid = None
		self.customer_props = None
		self.fields = None
		self.market_id = None
		self.page_no = None
		self.page_size = None
		self.props = None
		self.q = None
		self.status = None
		self.suite_items_str = None
		self.vertical_market = None

	def getapiname(self):
		return 'taobao.products.search'
