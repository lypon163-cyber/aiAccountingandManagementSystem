# 方法说明

## 数据来源
- AKShare 获取 A 股上市公司三大报表。

## 指标计算
- 盈利能力：ROA、ROE、毛利率、净利率
- 现金流质量：经营现金流/净利润、经营现金流/营业收入

## AI 角色
- AI 只负责将已计算好的指标翻译成自然语言解读。
- AI 不接触原始数据，不进行计算，不编造数字。
- 若 API 不可用，使用预设的 fallback 文字。

## 运行方式
- 在 GitHub Codespaces 中：`pip install -r requirements.txt` 然后 `streamlit run app.py`
- 部署到 Streamlit Cloud：连接 GitHub 仓库，设置 Secrets 中的 `DEEPSEEK_API_KEY`。
