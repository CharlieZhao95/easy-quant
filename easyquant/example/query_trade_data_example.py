# -*- coding:utf-8 -*-
"""
We could learn and try the following tasks:

    1. Pick a stock at random.
    2. Query historical trade data of this stock.
    3. Print all the dates when this stock closed 3% higher than opening.
    4. Print all the dates with a drop more than 2% from yesterday's close when this stock opened;
    5. Execute a simple strategy to trade stock and calc values at the end.
    6. Draw and mark the dates that we choose to purchase or sell stock in our figure.
Author: https://github.com/CharlieZhao95
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from easyquant.data.stock_metadata import *
from easyquant.data.trade_data_searcher import *
from easyquant.common.constants import *

# 1. Pick a stock at random.
stock_info = StockMetadata('sh.603986', '兆易创新', ['半导体', '芯片'])
searcher = TradeDataSearcher(stock_metadata=stock_info)


# 2. Query K-line data of this stock.
def query_historical_data_default():
    trade_info = TradeMetadata()  # default param to query data: 'date,code,open,high,low,close'
    k_data = searcher.query_stock_k_line_data(trade_metadata=trade_info).get_data()
    searcher.save_data_to_csv(data=k_data,
                              root_path="G:\\GitHub\\easy-quant\\ds",
                              info="default_example")
    return k_data


def query_historical_data_all():
    trade_all_info = TradeMetadata(query_param=QUERY_PARAM_ALL)
    k_data = searcher.query_stock_k_line_data(trade_metadata=trade_all_info).get_data()
    searcher.save_data_to_csv(data=k_data,
                              root_path="G:\\GitHub\\easy-quant\\ds",
                              info="all_example")
    return k_data


# 3. Print all the dates when this stock closed 3% higher than opening.
def query_dates_with_higher_price():
    # Set param to query data that we want.
    k_data = query_historical_data_all()
    res = []

    def check_higher(open_price, close_price):
        return (close_price - open_price) / close_price > 0.03

    # use iter object to traverse
    for index, row in k_data.iterrows():
        if check_higher(float(row['open']), float(row['close'])):
            res.append(row['date'])
    return res


# 4. Print all the dates with a drop more than 2% from yesterday's close when this stock opened.
def query_dates_with_lower_price_than_yesterday():
    k_data = query_historical_data_all()
    res = []

    def check_lower_than_yesterday(open_price, yesterday_price):
        return (yesterday_price - open_price) / yesterday_price > 0.02

    (last_index, last_row) = next(k_data.iterrows())
    for index, row in k_data.iterrows():
        if check_lower_than_yesterday(float(row['open']), float(last_row['close'])):
            res.append(row['date'])
        # save yesterday data
        last_index, last_row = index, row
    return res


