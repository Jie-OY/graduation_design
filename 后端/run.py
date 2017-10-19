# -*- coding: utf-8 -*-


""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: run.py 
@time: 2017/8/21 21:54 
"""

from app import app
from app import cache

# Check Configuring Flask-Cache section for more details
cache.init_app(app, config={'CACHE_TYPE': 'simple'})
# 输入 main，再按 Tab 自动补全下行
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
