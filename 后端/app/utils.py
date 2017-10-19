# -*- coding: utf-8 -*-


"""
    测试模块
    (因为基本都涉及到数据库操作，而且考虑到数据库的更改，不好直接assert判断是否相等)
    ~~~~~~~~~~~~~~~~
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: utils.py 
@time: 2017/8/25 10:13 
"""
from flask import g, jsonify
from app import app
from .aes import encrypt, decrypt
from . import logger
from functools import wraps
import re

# conn = g.db
# cursor = g.db.cursor()
# COLUMN = ('ID','Name', 'UserIPsd', 'UserISex', 'UserICode', 'UserIStudentNumber')
COLUMN = app.config['COLUMN']
# 提取选择题各个选项组成列表,changed:添加全角半角支持
pattern = re.compile(r'[A-Z](?:.*?)(?=[A-Z](?:\.|．))', re.S)


def get_info(UserICode):
    """
    通过用户名获取身份信息
    :param sCode:
    :return: 字典
    """
    row = g.cursor.execute("select * from dbo.tblUserInfo WHERE UserICode = ?", UserICode).fetchone()
    info = {c: getattr(row, c) for c in COLUMN}

    info['UserIPsd'] = decrypt(info['UserIPsd'])
    # print(info)
    return info


def put_info(UserICode, new_info):
    """
    根据用户名ID对应账号身份信息,因为可能修改了UserICode(账户名)
    :param UserICode: str type
    :param new_info: 客户端传过来的新的信息（已转为字典类型）
    :return:
    """
    # 学号不提供更改，去除 UserICode 字段判断
    # old_info = g.cursor.execute("select * from dbo.tblUserInfo WHERE ID = ?", ID).fetchone()
    # UserICode = old_info.UserICode
    old_info = get_info(UserICode)
    ID = old_info['ID']
    for i in (new_info, old_info):
        i['UserIPsd'] = encrypt(i['UserIPsd'])
    # print(old_info.ID, new_info, sep='\n')
    # 比较哪些prop被改变了
    try:
        for c in COLUMN:
            if c == 'ID':
                pass
            elif new_info[c] == old_info[c]:
                pass
            else:
                g.cursor.execute("UPDATE dbo.tblUserInfo SET {} = ? WHERE ID = ?".format(c), new_info[c], ID)
    except Exception as e:
        logger.error('[{}]信息修改失败: {}'.format(ID, e))
        return False
    g.db.commit()
    return True


def get_quiz_list():
    rows = g.cursor.execute("select ID,Name from dbo.tblCourseInfo WHERE ParentIndex = -1")
    # 形如{ 1: '微机原理与接口技术', 2: '微机原理与接口', 3: '数字逻辑与FPGA',}
    course_dict = {row.Name: row.ID for row in rows}
    # key是课程名，value是包含该课程所有章节的列表 {'数字逻辑与FPGA': ['第一章', '第二章', '第四章', '']
    course_chapter_dict = dict()
    for k, v in course_dict.items():
        r = g.cursor.execute("select Name from dbo.tblCourseInfo WHERE ParentIndex = ?", v)
        course_chapter_dict[k] = [m.Name for m in r]
    course_list = list(course_dict.keys())
    return course_list, course_chapter_dict


def get_quiz_items(chapter_name):
    """目前不会将答案这个字段发送给前端"""
    chapter_ID = g.cursor.execute("select ID from dbo.tblCourseInfo WHERE NAME = ?", chapter_name).fetchone().ID
    r = g.cursor.execute(
        "select ID,Type,Question from dbo.tblTestQuestion WHERE ChapterID = ? and DelFlag='False' ",
        chapter_ID)
    items = [list(i) for i in r]

    return formater(items)


def get_quiz_score(answers):
    """批改前端发送来的测试答案，得出分数（Todo）"""
    return '100'


def formater(items):
    """
    用于分割Question字段中的题目和选项（只针对选择题）
    rules:
        1.题目结尾跟一个换行符
        2.各选项之间以空格隔开，且选项内部不得含空白字符
    """
    global pattern
    for item in items:
        if item[1] == '选择题':
            # 只进行一次分割，下面是为什么这么做的例子
            # '8086CPU的控制线BHE#=0，地址线A0=0时，CPU：\nA.从偶地址开始完成8位数据传送\nB.从偶地址开始完成16位数据传送 \n
            title, choices = item[2].split('\n', 1)
            # print('choices' + choices)
            item[2] = title
            choices += 'A.'  # 为了re，见简书
            choices_list = pattern.findall(choices.lstrip())
            print(choices_list)
            for i in choices_list:
                d = {'label': i, 'value': i[0]}  # 为了配合前端Vue使用到的mt-checklist的数据格式
                item.append(d)
    return items


# 验证登录的有效性
def verify(UserICode, UserIPsd):
    row = g.cursor.execute("select UserIPsd from dbo.tblUserInfo WHERE UserICode = ?", UserICode).fetchone()
    if row:
        if encrypt(UserIPsd) == row.UserIPsd:
            return True, ''
        else:
            return False, '密码不正确'
    else:
        return False, '用户名不正确'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.UserICode is None or g.ID is None:
            return jsonify({'errmsg': '请先登录'}), 401
        return f(*args, **kwargs)

    return decorated_function


if __name__ == "__main__":
    def test():
        r = get_info('2014211674')
