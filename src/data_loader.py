"""
data_loader.py
通过 AKShare 获取 A 股上市公司三大报表数据。
"""

import akshare as ak
import pandas as pd


def get_financial_statements(stock_code: str, years: int = 4) -> dict:
    """
    获取指定股票的利润表、资产负债表、现金流量表。

    参数:
        stock_code: 6 位股票代码，如 "600519"
        years: 拉取最近多少年

    返回:
        {
            "income": DataFrame,
            "balance": DataFrame,
            "cashflow": DataFrame,
        }
    """
    result = {}

    # 利润表
    result["income"] = ak.stock_financial_report_sina(
        stock=stock_code, symbol="利润表"
    ).head(years)

    # 资产负债表
    result["balance"] = ak.stock_financial_report_sina(
        stock=stock_code, symbol="资产负债表"
    ).head(years)

    # 现金流量表
    result["cashflow"] = ak.stock_financial_report_sina(
        stock=stock_code, symbol="现金流量表"
    ).head(years)

    return result
