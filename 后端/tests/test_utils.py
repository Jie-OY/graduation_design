# -*- coding: utf-8 -*-


""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: test_utils.py 
@time: 2017/8/25 1:40 
"""
from app.utils import get_info, get_quiz_list, get_quiz_items
from app.api import get_db
from app import app
from flask import g
import pytest


def set_g():
    g.db = get_db()
    g.cursor = g.db.cursor()


def test_get_quiz_items():
    with app.app_context():
        set_g()
        # r = get_quiz_items('第一章 概述')
        r = get_quiz_items('第二章 80x86微处理器')
    print(r)


def test_get_quiz_list():
    with app.app_context():
        set_g()
        course_dict, course_chapter_dict = get_quiz_list()
    print(course_dict, course_chapter_dict, sep='\n')


def test_get_info_func():
    with app.app_context():
        set_g()
        r = get_info('2014211674')
    print(r)
