"""
ai_interpreter.py
AI 解读层。只接收已计算好的指标文字，生成自然语言解读。
AI 不接触原始数据，不进行计算。
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

SYSTEM_PROMPT = """你是一个财务报表分析助手。
你只能解释我提供的数字，不能编造任何未给出的数据。
不要进行计算，不要引用外部数据。
用本科财务报表分析的语言，简洁地写一段解读。
如果数据中存在异常趋势，指出研究者应关注的方向。"""


def interpret(metric_text: str, fallback: str = "") -> str:
    """
    输入已计算好的指标文字描述，返回 AI 生成的解读。
    如果没有 API Key 或调用失败，返回 fallback 文字。
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": metric_text},
            ],
            stream=False,
        )
        return response.choices[0].message.content
    except Exception:
        return fallback
