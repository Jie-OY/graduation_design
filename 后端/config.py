# -*- coding: utf-8 -*-

import os
import datetime

# 此文件所在文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: config.py 
@time: 2017/8/20 22:39 
"""
SECRET_KEY = 'hfut.shilei.oyj.wjc.'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 数据库配置
DATABASE_NAME = 'MvcTywzV2'
DATABASE_UID = 'python'
DATABASE_PWD = 'ojeveryday'
DATABASE_DRIVER = '{SQL Server Native Client 11.0}'
DATABASE_IP_PORT = '127.0.0.1,1433'
uri = r'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(DATABASE_DRIVER, DATABASE_IP_PORT,
                                                              DATABASE_NAME, DATABASE_UID,
                                                              DATABASE_PWD)
SQLSERVER_DATABASE_URI = os.environ.get('SQLSERVER_URI') or uri
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON_AS_ASCII = False    # 使得json数据可以正常显示中文
SESSION_COOKIE_HTTPONLY = True

# 一个持久化的会话的生存时间，作为一个 datetime.timedelta 对象。\
# 从 Flask0.8 开始 也可以用一个整数来表示秒。
# session 15天没有登录过就过期
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=15)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COLUMN = ('ID', 'Name', 'UserIPsd', 'UserISex', 'UserICode', 'UserIStudentNumber')
