# -*- coding:utf-8 -*-
"""
Definition of the stock metadata.

Author: https://github.com/CharlieZhao95
"""
from easyquant.common.constants import *


class TradeMetadata(object):
    """
    Stock trade metadata.

    description: description of those data
    start_time: trade start date
    end_time: trade end date
    trade_data: `pandas.DataFrame` format data
    """

    def __init__(self, start_time=START_TIME_DEFAULT,
                 end_time=END_TIME_DEFAULT,
                 description=None,
                 trade_data=None,
                 query_param=QUERY_PARAM_DEFAULT):
        self._start_time = start_time
        self._end_time = end_time
        self._description = description
        self._trade_data = trade_data
        self._query_param = query_param

    @property
    def trade_time(self):
        return [self._start_time, self._end_time]

    @property
    def description(self):
        return self._description

    @property
    def trade_data(self):
        return self._trade_data

    @property
    def query_param(self):
        return self._query_param


class StockMetadata(object):
    """
    Stock metadata contains:
        name: stock name
        code: stock code
        tags: use tags to classify stock

    >>> stock = StockMetadata('sh.603986', '兆易创新', ['半导体', '芯片'])
    """

    def __init__(self, code: str, name: str = None, tags=None):
        if tags is None:
            tags = []
        self._code = code
        self._name = name
        self._tags = tags
        self._trade_data = {}

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def tags(self):
        return self._tags

    @property
    def trade_data(self):
        return self._trade_data

    def append_trade_data(self, key, trade_data):
        self._trade_data[key] = trade_data
