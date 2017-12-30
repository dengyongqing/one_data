# -*- coding:utf-8 -*-  
from rqalpha import run_file
from rqalpha.utils import scheduler
from init import init_data
import schedule
import time
import datetime
import pandas as pd
import sys, os
import threading
import multiprocessing
from mail.mail import send_mail

strategy_file_path = "./one_strategy/strategies/happy.py"

def start():
    try:
        os.system('rqalpha update_bundle')
        init_data()
        send_mail('数据初始化成功！', 'init')
    except Exception as e:
        print(e)

def get_today():
    now = datetime.datetime.now()
    year = int(now.strftime('%Y'))  
    today = now.strftime('%Y-%m-%d') 
    return today

start()
schedule.every().day.at("16:00").do(start).tag('my_job')
while 1:
    schedule.run_pending()
    time.sleep(1)