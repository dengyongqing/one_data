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
        # data.to_sql('stock_basics',engine,index=True,if_exists='replace')
        print("I'm working......插入成功")
        if 0:
            print("okkkkkkkk")
        else:
            print("xxxxxxxxxx")
        print(not len(data[data["name"]=="东方财富11"]["name"]))
        # print(data[data["name"]=="东方财富"].name[0])
        # for index, row in data.iterrows():   # 获取每行的index、row
        #     # if_exists = 'append'
        #     # if count == 1: 
        #     #     if_exists = 'replace'
        #     # for col_name in data.columns:
        #     # print("开始获取行情数据......" + row.name)
        #     get_k_data = ts.get_k_data(row.name, start='1990-12-19')
        #     myData = pd.DataFrame(get_k_data)
        #     ma_list = ta.MA(myData.close, timeperiod=30, matype=0)
        #     # last = ma_list.tail(1)
        #     print(ma_list[28])

    except Exception as e:
        print(e)

init() 
