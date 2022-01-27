# -*- coding:utf-8 -*-
"""
Query stock trade data bases on existing platforms.

Author: https://github.com/CharlieZhao95
"""
import os
import baostock as bs

from baostock.common import contants as bs_const

from easyquant.data.stock_metadata import *
from easyquant.common.logger import *

logger = logging.getLogger(__name__)


class TradeDataSearcher(object):
    """
    Query stock trade data bases on baostock package.

    Example to use constructor and query trade data:

    >>> stock_info = StockMetadata('sh.603986', '兆易创新', ['半导体', '芯片'])
    >>> searcher = TradeDataSearcher(stock_metadata=stock_info)
    >>> trade_info = TradeMetadata()
    >>> k_data = searcher.query_stock_k_line_data(trade_metadata=trade_info)
    >>> k_data is not None
    True
    """

    def __init__(self, stock_metadata: StockMetadata):
        logger.info("Trade data searcher is running.")

        self.stock_metadata = stock_metadata
        # login database system
        lg = bs.login()
        if lg.error_code != bs_const.BSERR_SUCCESS:
            logger.warning("login respond error code {}, "
                           "with msg {}".format(lg.error_code, lg.error_msg))
        else:
            logger.info("login success")

    def query_stock_k_line_data(self, trade_metadata: TradeMetadata):
        """ Query stock K-line data from baostock """
        k_data = bs.query_history_k_data_plus(self.stock_metadata.code,
                                              trade_metadata.query_param,
                                              start_date=trade_metadata.trade_time[0],
                                              end_date=trade_metadata.trade_time[1])

        if k_data.error_code != bs_const.BSERR_SUCCESS:
            logger.warning("query {} k history data fail, respond error code {}, "
                           "with msg {}".format(self.stock_metadata.code, k_data.error_code, k_data.error_msg))
            return None
        return k_data

    def save_data_to_csv(self, data, root_path, file_name="default"):
        """ Save stock historical data to csv file """
        dir_path = "{}\\{}_{}".format(root_path,
                                      self.stock_metadata.code,
                                      self.stock_metadata.name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        save_path = "{}\\{}.csv".format(dir_path, file_name)
        data.to_csv(save_path, index=False)
