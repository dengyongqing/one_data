# -*- coding:utf-8 -*-  
from sqlalchemy import create_engine
from django.http import HttpResponse
import json
import pandas as pd
import numpy as np
import tushare as ts
import talib as ta
import time,sched
import schedule
import time
import datetime
import threading
import sys, os

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import json
import random
from db.db import get_db_connect
from math import isnan

now = datetime.datetime.now()
year = int(now.strftime('%Y'))  
today = now.strftime('%Y-%m-%d')  
now = now.strftime("%Y-%m-%d %H:%M:%S")

# engine = create_engine('postgresql://postgres:142857@47.93.193.128:5432/tushare') 
engine = get_db_connect()
# engine = create_engine('postgresql://tushare@localhost:5432/tushare')
# 交易数据
def init():
    try:
        print("I'm working......交易数据")
        # 股票列表
        stock_basics = ts.get_stock_basics()
        y_close = 0
        up_count = 0
        down_count = 0
        data = pd.DataFrame(stock_basics)
        data = data[200: 205]
        # data.to_sql('stock_basics',engine,index=True,if_exists='replace')
        print("I'm working......插入成功")
       
        # print(not len(data[data["name"]=="东方财富11"]["name"]))
        # print(data[data["name"]=="东方财富"].name[0])
        for index, row in data.iterrows():   # 获取每行的index、row
            # if_exists = 'append'
            # if count == 1: 
            #     if_exists = 'replace'
            # for col_name in data.columns:
            # print("开始获取行情数据......" + row.name)
            get_k_data = ts.get_k_data(row.name, start='1990-12-19')
            my_data = pd.DataFrame(get_k_data)
            my_data_array = np.array(my_data.close)
            ma_list = ta.MA(np.array(my_data.close), timeperiod=30, matype=0)
            ma_list_len = len(ma_list)
                
            # print(isnan(ma_list[0]))
            if isnan(ma_list[len(ma_list)-1]):
                continue
        
            if (my_data_array[len(my_data_array)-1] > ma_list[len(ma_list)-1]):
                up_count = up_count + 1
                print("股票代码：" + row.name)
                print("收盘价：" + str(my_data_array[len(my_data_array)-1]))
                print("均线收盘价：" + str(ma_list[len(ma_list)-1]))
                print("第" + str(up_count) + "个超过均线的股票")
            else:
                down_count = down_count + 1
        
        if_exists = 'append'
        get_k_data = ts.get_k_data("sh000001", start='2018-08-08')

        print("start")
        df_dict = { "up_count": [up_count], "down_count": [down_count], "date": [get_k_data["date"][0]] }
        my_data = pd.DataFrame(df_dict)
        print(get_k_data["date"][0])

        # myData = pd.DataFrame(get_k_data)
        # my_data.to_sql('up_count',engine,index=True,if_exists=if_exists)
        # print("插入成功")
        
        # print("在30日均线上方的股票：", up_count)

    except Exception as e:
        print("error")

init() 
