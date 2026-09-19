"""
app.py
财务体检研究工具 - Streamlit 主入口。
"""

import streamlit as st
import pandas as pd
from src.data_loader import get_financial_statements
from src.metrics import compute_profitability, compute_cashflow_quality
from src.charts import line_chart, bar_chart
from src.ai_interpreter import interpret

st.set_page_config(page_title="财务体检研究工具", layout="wide")
st.title("财务体检研究工具")
st.caption("输入股票代码，自动拉取财报并计算财务比率")

stock_code = st.text_input("股票代码", placeholder="例如：600519")

if st.button("开始分析"):
    if not stock_code:
        st.warning("请输入股票代码")
    else:
        with st.spinner("正在拉取财报数据..."):
            try:
                data = get_financial_statements(stock_code, years=4)
            except Exception as e:
                st.error(f"数据拉取失败：{e}")
                st.stop()

        income = data["income"]
        balance = data["balance"]
        cashflow = data["cashflow"]

        st.success("数据拉取完成")

        # 展示原始报表（可选）
        with st.expander("查看原始报表"):
            st.subheader("利润表")
            st.dataframe(income)
            st.subheader("资产负债表")
            st.dataframe(balance)
            st.subheader("现金流量表")
            st.dataframe(cashflow)

        # 计算指标
        try:
            profit_metrics = compute_profitability(income, balance)
            cash_metrics = compute_cashflow_quality(income, cashflow)
        except Exception as e:
            st.error(f"指标计算失败，请检查列名映射：{e}")
            st.stop()

        # 盈利能力图表
        st.subheader("盈利能力趋势")
        fig_ profit = line_chart(profit_metrics, title="盈利能力")
        st.plotly_chart(fig_profit, use_container_width=True)

        # 现金流质量图表
        st.subheader("现金流质量趋势")
        fig_cash = bar_chart(cash_metrics, title="现金流质量")
        st.plotly_chart(fig_cash, use_container_width=True)

        # AI 解读
        st.subheader("AI 辅助解读")
        metric_text = f"""
        公司股票代码：{stock_code}
        盈利能力指标（近四年）：
        ROA: {profit_metrics['ROA'].tolist()}
        ROE: {profit_metrics['ROE'].tolist()}
        毛利率: {profit_metrics['毛利率'].tolist()}
        净利率: {profit_metrics['净利率'].tolist()}

        现金流质量指标（近四年）：
        经营现金流/净利润: {cash_metrics['经营现金流/净利润'].tolist()}
        经营现金流/营业收入: {cash_metrics['经营现金流/营业收入'].tolist()}

        请用本科财务报表分析的语言，写一段简洁的解读，指出利润质量和现金流的变化趋势，并提示研究者应关注什么。
        """
        fallback = "AI 解读暂不可用，请检查 API Key 配置。"
        interpretation = interpret(metric_text, fallback=fallback)
        st.write(interpretation)
