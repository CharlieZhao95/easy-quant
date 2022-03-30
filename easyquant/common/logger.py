# -*- coding:utf-8 -*-
"""
easy-quant logger module.

Author: https://github.com/CharlieZhao95
"""
import logging


def log_init():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


log_init()
