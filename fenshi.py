# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:33:15 2019

@author: dell
"""

import requests
from bs4 import BeautifulSoup
import time
import re

rs = requests.get('https://stock2.finance.sina.com.cn/futures/api/jsonp.php/var%20t1nf_RB0=/InnerFuturesNewService.getMinLine?symbol=RB0')
time.sleep(3)
infos = rs.text
p1 = re.compile(r'[(](.*?)[)]', re.S)
p2 = re.compile(r':.*', re.S)
list_all = re.findall(p1, infos)

list_re = list_all[0].replace('[','')
list_rt = list_re.replace(']','')

listall = list_rt.split(',')
openlist = listall[0:7]
zuoshous = openlist[5]
zuoshou = float(re.sub('"','',zuoshous))
kaipans = openlist[1]
kaipan = float(re.sub('"','',kaipans))



list_sy = listall[7:]
num =int( len(list_sy)/5)
for i in range(num):
    timess = list_sy[5*i]
    times = re.sub('"','',timess)
    
    nowjias = list_sy[5*i+1]
    nowjia = float(re.sub('"','',nowjias))
    
    
    avagejias = list_sy[5*i+2]
    avagejia = float(re.sub('"','',avagejias))
    
    
    amounts = list_sy[5*i+3]
    amount = float(re.sub('"','',amounts))
    
    chicangs = list_sy[5*i+4]
    chicang = float(re.sub('"','',chicangs))
    
    print(times,nowjia,avagejia,amount,chicang)
