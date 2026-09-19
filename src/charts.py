"""
charts.py
使用 plotly 生成图表。
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def line_chart(metrics: dict, title: str = "") -> go.Figure:
    df = pd.DataFrame(metrics)
    df["年份"] = df.index  # 假设索引就是年份
    df_melt = df.melt(id_vars=["年份"], var_name="指标", value_name="数值")
    fig = px.line(df_melt, x="年份", y="数值", color="指标", title=title, markers=True)
    return fig

def bar_chart(metrics: dict, title: str = "") -> go.Figure:
    df = pd.DataFrame(metrics)
    df["年份"] = df.index
    df_melt = df.melt(id_vars=["年份"], var_name="指标", value_name="数值")
    fig = px.bar(df_melt, x="年份", y="数值", color="指标", title=title, barmode="group")
    return fig
