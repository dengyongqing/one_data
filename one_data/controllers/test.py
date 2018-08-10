# -*- coding:utf-8 -*-  
import tushare as ts
import pandas as pd
import urllib
from django.http import HttpResponse

def reconice():
    stock_basics = ts.get_stock_basics()
    # data = pd.DataFrame(stock_basics)

    for index, row in stock_basics.iterrows():   # 获取每行的index、row
        # if row.name in question:
        #     return HttpResponse("name" + row.name)
        # if row.code in question:
        #     return HttpResponse("code:" + row.code)
        print(urllib.unquote("%E9%82%93%E6%B0%B8%E5%BA%86"));
        # print("name:", row.name);
    # return HttpResponse("我还不知道呢")



reconice()