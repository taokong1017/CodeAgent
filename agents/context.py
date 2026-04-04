class Context:
    """
    标准Agent运行上下文，执行任务全过程的状态与记忆
    """
    # 唯一标识
    session_id: str       # 会话 ID
    user_id: str          # 用户 ID
    agent_id: str         # 智能体 ID

    # 核心记忆
    messages: list        # 对话历史
    current_task: dict    # 当前正在执行的任务
    task_history: list    # 已完成任务历史

    # 状态控制
    state: str            # 运行状态：idle / thinking / executing / finished
    current_step: int     # 执行到第几步
    max_steps: int        # 最大执行步数

    # 环境与权限
    tools: list           # 可用工具列表
    variables: dict       # 自定义变量（可读写）
    config: dict          # 模型/行为配置

    # 版本与回溯
    version: int          # 上下文版本号
    versions: list        # 历史快照（用于回滚、重试）
