# -*- coding: utf-8 -*-
from django.shortcuts import render
from CONSTANT import *
from test import *
# import socket
# import threading
# import time
# import json
# import re
# def testreq(q):
    # req=TbkItemGetRequest( 'gw.api.taobao.com',80 )
    # req.set_app_info(appinfo(appkey,serect))
    # req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
    # req.q="女装"
    # req.q=q
    # resp= req.getResponse()
    # print (resp)
    # b=json.dumps(resp).decode('unicode-escape')
    # print type(b)
    # print b
    # return resp,b
def index(request):
    return render(request, 'search/index.html',)
def resp(request):
    keywd=request.POST.get('search',False)
    a,b=testreq(keywd)
    a=a["tbk_item_get_response"]
    a=a["results"]
    a=a["n_tbk_item"]
    for i in range(len(a)):
        a[i]={k:a[i][k] for k in ('title','pict_url')}
    return render(request, 'search/resp.html',{'a':a,'keywd':keywd})
    # return render(request,'search/resp.html',{'keywd':keywd})
# print testreq("haha")
