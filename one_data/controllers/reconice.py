# -*- coding:utf-8 -*-  
import tushare as ts
import pandas as pd
import urllib
from django.http import HttpResponse

def reconice(request):
    # request.encoding='utf-8'
    question=request.GET.get('question')
    stock_name=request.GET.get('stock_name')
    # question=question.encode('utf-8')
    question=urllib.unquote(question)
    stock_name=urllib.unquote(stock_name)
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)

    for index, row in data.iterrows():   # 获取每行的index、row
        if row["name"] == stock_name:
            return HttpResponse(row.name)

    return HttpResponse("我还不知道呢")



