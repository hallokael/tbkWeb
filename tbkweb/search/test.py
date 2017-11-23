# -*- coding: utf-8 -*-
import top.api
from CONSTANT import *
import socket
import threading
import time
import json
import re
def testreq():
    req=top.api.TbkItemGetRequest( 'gw.api.taobao.com',80 )
    req.set_app_info(top.appinfo(appkey,serect))
    req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
    req.q="女装"
    resp= req.getResponse()
    #print (resp)
    b=json.dumps(resp).decode('unicode-escape')
    print (type(b))
    print (b)
    return resp,b
#resp=str( resp )
#print(type(resp))
#print(resp)
#e=str(resp)
#result,number=re.subn("u '", "'", e)
##print (result,number)
#e.decode('utf-8')
#print (e)
def tcplink(sock, addr):
    print('Accept from %s:%s' % addr)
    sock.send(b'Welcome!!!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode( 'utf-8' )=='exit':
            break
        sock.send( ( 'Hello,%s!'%data.decode( 'utf-8' ) \
                     ).encode('utf-8') )
    sock.close()
    print('Connection from %s:%s closed.'%addr)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(( '127.0.0.1', 9999 ))
# s.listen(5)
# print('Waiting')
# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock, addr))
# t.start()
