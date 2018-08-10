# -*- coding:utf-8 -*-  
import tushare as ts
import pandas as pd
import urllib
from django.http import HttpResponse

def reconice(request):
    # request.encoding='utf-8'
    question=request.GET.get('question')
    stock_name=request.GET.get('stock_name')
    stock_property=request.GET.get('stock_property')
    # question=question.encode('utf-8')
    question=urllib.unquote(question)
    stock_name=urllib.unquote(stock_name)
    stock_property=urllib.unquote(stock_property)
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)

    for index, row in data.iterrows():   # 获取每行的index、row
        pe = row["pe"]
        pb = row["pb"]
        # close = row["close"]
        code = row.name
        if row["name"] == stock_name:
            if stock_property == "pe":
                return HttpResponse(pe)
            elif stock_property == "pb":
                return HttpResponse(pb)
            # elif stock_property == "股价":
            #     return HttpResponse(close)
            elif stock_property == "代码":
                return HttpResponse(code)
            

    return HttpResponse("我还不知道呢")



