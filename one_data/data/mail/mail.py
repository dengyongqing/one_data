# -*- coding:utf-8 -*-  
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import traceback
import smtplib
import json
import random

import time
import datetime

mail_host="smtp.aliyun.com"  #设置服务器
mail_user="dengyongqing@aliyun.com"    #用户名
mail_pass="Dfzr.Rrqs@1"   #口令 

sender = ['dengyongqing@aliyun.com']
receivers = ['dengyongqing_json@aliyun.com']
# receivers = [
#     'dengyongqing@aliyun.com', 
#     '1148674087@qq.com',    #邓永康
#     '13816904330@163.com', #姜飞标
#     '317223343@qq.com',    #陈贵
#     '312204337@qq.com',    #汤东强
#     '511868788@qq.com',    #田世峰
#     '448943531@qq.com',    #杨少文
#     '196863227@qq.com',    #joshua
#     ]

def send_mail(msg, flag):
    for mail in receivers:   # 获取每行的index、row
        try:
            if flag == 'init':
                send_notice_mail(sender, mail, msg)
                
        except Exception as e:
            print(e)
    
def send_notice_mail(sender, receivers, msg):
    print("I'm working......发送选股邮件")

    message = MIMEText(msg, 'html', 'utf-8')
    message['From'] = formataddr(["小安", "dengyongqing@aliyun.com"])
    message['To'] =  Header('小安', 'utf-8')
    
    now = get_now()  
    subject = '小安数据' + '(' + now + ')'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except (smtplib.SMTPException, Exception) as e:
        print (e)
        print ("Error: 无法发送邮件")
    print("发送邮件......done")

def get_now():
    now = datetime.datetime.now()
    year = int(now.strftime('%Y'))  
    format_now = now.strftime('%Y-%m-%d %H:%M:%S') 
    return format_now

def get_today():
    now = datetime.datetime.now()
    year = int(now.strftime('%Y'))  
    today = now.strftime('%Y-%m-%d') 
    return today

__all__ = ['send_mail']