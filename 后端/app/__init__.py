# -*- coding: utf-8 -*-


""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: __init__.py.py 
@time: 2017/8/20 22:37 
"""
from flask import Flask, g
import config
from .log import logger
from flask_cache import Cache
import pyodbc

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)

app.config.from_object(config)


def db_connect():
    try:
        conn = pyodbc.connect(app.config['SQLSERVER_DATABASE_URI'])
    except Exception as e:
        logger.error('database connection failed --- {}'.format(e))
    return conn


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


from . import api
