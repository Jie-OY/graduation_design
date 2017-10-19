# -*- coding: utf-8 -*-


"""
创建一个名为`hfut`的logger.含有两个Handler.
一个用于输出日志记录到文件中，级别为Warning以上
另一个用于输出日志记录到sys.stderr中，级别为Info以上
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: log.py 
@time: 2017/8/21 22:04 
"""
import logging

logger = logging.getLogger('hfut')

logger.setLevel(logging.INFO)

handler = logging.FileHandler('hfut.log', encoding='utf-8')
print_handler = logging.StreamHandler()

handler.setLevel(logging.WARNING)
print_handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
print_handler_formatter = logging.Formatter('[%(asctime)s] -%(filename)s - %(message)s')

handler.setFormatter(formatter)
print_handler.setFormatter(print_handler_formatter)

logger.addHandler(handler)
logger.addHandler(print_handler)


if __name__ == '__main__':
    logger.error('test')
    logger.info('info')