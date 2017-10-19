# -*- coding: utf-8 -*-


""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: api.py
@time: 2017/8/24 22:44 
"""

from . import app, db_connect, cache
from .log import logger
from flask import g, request, session, render_template, jsonify
from .utils import verify, get_info, put_info, get_quiz_list, login_required, get_quiz_items, get_quiz_score


@app.before_request
def session_db_permanent():
    """
    在每次请求之前将session持久化设置为True，方会启用app.config中的session lifetime
    在每次请求之前获取数据库连接 g.db
    """
    session.permanent = True
    g.db = get_db()
    g.cursor = g.db.cursor()
    g.UserICode = session.get('UserICode', None)
    g.ID = session.get('ID', None)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db'):
        return db_connect()
    return g.db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    UserICode = request.json.get('UserICode', None)
    UserIPsd = request.json.get('UserIPsd', None)
    # print(UserICode, UserIPsd)
    verified, msg = verify(UserICode, UserIPsd)

    if verified:
        session['UserICode'] = UserICode
        info = get_info(UserICode)
        # print(info)
        session['ID'] = info['ID']
        return jsonify({'info': info, 'errmsg': ' '}), 200
    else:
        return jsonify({"errmsg": msg}), 401  # 401,凭据无效
        # auth_info = request.get_json()


@app.route('/info', methods=['GET', 'PUT'])
@login_required
def info():
    # try:
    #     current_user = session['UserICode']
    #     current_user_ID = session['ID']
    #     print(current_user, current_user_ID)
    # except:
    #     return jsonify({'errmsg': '请先登录'}), 401
    current_user = g.UserICode
    if request.method == 'GET':
        return jsonify({'info': get_info(current_user)}), 200

    if request.method == 'PUT':
        new_info = request.get_json()  # json.loads(data, object_pairs_hook=OrderedDict)
        print('request json', request.get_json())  # type: dict
        success = put_info(current_user, new_info)
        if success:
            info = get_info(new_info['UserICode'])
            session['UserICode'] = info['UserICode']
            return jsonify({'info': info}), 200
        else:
            return jsonify({'errmsg': '修改失败 >_<|||'}), 400


@app.route('/quiz/list')
@cache.cached(timeout=50)
def quiz_list():
    """
    设置了50s的缓存
    :return: json
    """
    try:
        course_list, course_chapter_dict = get_quiz_list()
        return jsonify(course_list=course_list, course_chapter_dict=course_chapter_dict), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'errmsg': '获取接口数据失败'}), 400


@app.route('/quiz/items/')
@app.route('/quiz/items/<chapter_name>')
@login_required
def quiz_items(chapter_name=None):
    """
    注意这个函数装载了两个路由，当前端传过来的章节name为空时就会
    匹配第一个路由"""
    # print(chapter_name)
    if chapter_name:
        items = get_quiz_items(chapter_name)
        return (jsonify(items=items), 200) if len(items) != 0 else (jsonify(errmsg='题库为空'), 400)
    else:
        return jsonify(errmsg='章节选择为空'), 400


@app.route('/quiz/check', methods=['POST'])
def quiz_check():
    answers = request.get_json()
    print(answers)
    try:
        score = get_quiz_score(answers)
    except Exception as e:
        logger.error(e)
        return jsonify(errmsg='Some Wrong'), 400
    return jsonify(score=score), 200


if __name__ == "__main__":
    def test():
        r = get_info('2014211674')
