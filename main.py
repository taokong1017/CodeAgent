from agents.basic_agent import BasicAgent
import os

if __name__ == "__main__":
    agent = BasicAgent(
        model=os.getenv("OPENAI_MODEL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        system_prompt="你是一个C语言开发专家",
    )

    response = agent.chat("请实现红黑树")
    print(response)
