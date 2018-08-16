# -*- coding:utf-8 -*-  
import tushare as ts
import pandas as pd
import urllib
from django.http import HttpResponse

def ma_up_count(request):
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

    # for index, row in data.iterrows():   # 获取每行的index、row
    if  (len(data[data["name"]==stock_name].index)):
        if stock_property == "code":
            return HttpResponse(data[data["name"]==stock_name].index[0])
        else:
            target = data[data["name"]==stock_name][stock_property]
            if not (len(target)):
                return HttpResponse("请输入例句如下：股票中国平安的市盈率，中国平安股票的市盈率，等等")
            else:
                # data[data["name"]=="东方财富"]["pe"][0]
                return HttpResponse(target[0])
                # return HttpResponse(row[stock_property])
                
    return HttpResponse("请输入例句如下：股票中国平安的市盈率，中国平安股票的市盈率，等等")


