"""
charts.py
使用 plotly 生成图表。
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def line_chart(metrics: dict, title: str = "") -> go.Figure:
    """
    绘制多条折线图。metrics 是 {指标名: Series} 的字典。
    """
    df = pd.DataFrame(metrics)
    # 假设索引是年份，如果不是，需要调整
    df = df.reset_index().rename(columns={"index": "年份"})
    fig = px.line(df, x="年份", y=df.columns[1:], title=title, markers=True)
    return fig


def bar_chart(metrics: dict, title: str = "") -> go.Figure:
    """
    绘制柱状图。metrics 是 {指标名: Series} 的字典。
    """
    df = pd.DataFrame(metrics)
    df = df.reset_index().rename(columns={"index": "年份"})
    fig = px.bar(df, x="年份", y=df.columns[1:], title=title, barmode="group")
    return fig
