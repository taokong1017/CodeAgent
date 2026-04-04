# agents/basic_agent.py
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from typing import List


class BasicAgent:
    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        api_key: str = None,
        base_url: str = None,
        tools: List = None,
        system_prompt: str = "你是一个专业的AI助手",  # 系统提示
    ):
        self.llm = ChatOpenAI(
            model=model, api_key=api_key, base_url=base_url, temperature=0
        )

        if tools is None:
            tools = []

        self.agent = create_agent(
            model=self.llm, tools=tools, system_prompt=system_prompt, debug=False
        )

    def chat(self, question: str) -> str:
        """对话：只返回纯文本内容"""
        result = self.agent.invoke(
            {"messages": [{"role": "user", "content": question}]}
        )

        return result["messages"][-1].content
