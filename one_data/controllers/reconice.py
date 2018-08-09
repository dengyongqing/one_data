# -*- coding:utf-8 -*-  
import tushare as ts
import pandas as pd
from django.http import HttpResponse

def reconice(request):

    question=request.GET.get('question')
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)

    for index, row in data.iterrows():   # 获取每行的index、row
        if row.name in question:
            return HttpResponse("name" + row.name)
        if row.code in question:
            return HttpResponse("code:" + row.code)

    return HttpResponse("我还不知道呢，你可以教我吗？“)



