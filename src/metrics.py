"""
metrics.py
财务比率计算。所有计算为确定性逻辑，不调用 AI。
"""

import pandas as pd


def _find_column(df: pd.DataFrame, candidates: list) -> str:
    """从 DataFrame 中查找第一个匹配的列名。"""
    for col in df.columns:
        for cand in candidates:
            if cand in col:
                return col
    raise KeyError(f"未找到列，候选：{candidates}，实际列：{list(df.columns)}")


def compute_profitability(income: pd.DataFrame, balance: pd.DataFrame) -> dict:
    """
    盈利能力指标：ROA、ROE、毛利率、净利率。
    """
    revenue_col = _find_column(income, ["营业收入", "营业总收入"])
    cost_col = _find_column(income, ["营业成本", "营业总成本"])
    net_profit_col = _find_column(income, ["净利润"])
    total_assets_col = _find_column(balance, ["资产总计", "总资产"])
    equity_col = _find_column(balance, ["所有者权益", "股东权益", "净资产"])

    revenue = income[revenue_col]
    cost = income[cost_col]
    net_profit = income[net_profit_col]
    total_assets = balance[total_assets_col]
    equity = balance[equity_col]

    return {
        "ROA": net_profit / total_assets,
        "ROE": net_profit / equity,
        "毛利率": (revenue - cost) / revenue,
        "净利率": net_profit / revenue,
    }


def compute_cashflow_quality(income: pd.DataFrame, cashflow: pd.DataFrame) -> dict:
    """
    现金流质量指标：经营现金流/净利润、经营现金流/营业收入。
    """
    revenue_col = _find_column(income, ["营业收入", "营业总收入"])
    net_profit_col = _find_column(income, ["净利润"])
    ocf_col = _find_column(cashflow, ["经营活动产生的现金流量净额", "经营现金流"])

    revenue = income[revenue_col]
    net_profit = income[net_profit_col]
    ocf = cashflow[ocf_col]

    return {
        "经营现金流/净利润": ocf / net_profit,
        "经营现金流/营业收入": ocf / revenue,
    }
