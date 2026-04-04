from agents.agent import Agent
from agents.context import Context
import os

if __name__ == "__main__":
    agent = Agent(
        model=os.getenv("OPENAI_MODEL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        system_prompt="你是一个C语言开发专家",
    )

    context = Context()

    for text in agent.stream_chat(
        f"请完成红黑树组件设计、接口设计和数据结构设计，不需要编码"
    ):
        print(text, end="", flush=True)
    print()
