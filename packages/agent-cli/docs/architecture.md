# Agent-CLI Architecture

## 项目概述

Agent-CLI 是一个 Claude Code 的最小实现，具有丰富的工具系统、任务规划、子代理编排和技能系统支持。
该项目采用现代 Python 架构设计，强调依赖注入、接口抽象和线程安全。

**核心特性：**

- 🛠️ 12+ 内置工具（Bash、Read、Write、Edit、Glob、Grep、WebSearch、WebReader、TaskUpdate、Task、Skill）
- 🎯 三种子代理类型（Explore、Plan、Code）
- 📚 三层技能系统（描述、内容、资源）
- 📋 任务管理和追踪
- 🔄 线程安全的中断机制
- 🎨 Textual TUI 界面

## 架构设计

### 核心原则

1. **依赖注入** - 所有依赖通过构造函数传递，不使用单例模式
2. **接口抽象** - 使用 Protocol 定义接口契约，实现松耦合
3. **类型安全** - 完整的类型注解，使用 TypeVar 和 dataclass
4. **线程安全** - Agent 循环支持中断，使用锁保护共享状态
5. **关注点分离** - UI、业务逻辑、工具执行相互独立

### 模块结构

```bash
agent_cli/
├── __init__.py          # 入口点
├── agent.py             # 核心 Agent 实现
├── config.py            # 配置管理
├── interfaces.py        # 接口定义（Protocol）
├── tools.py             # 工具定义和执行
├── skill.py             # 技能系统
├── task.py              # 任务管理
├── subagent.py          # 子代理定义
├── system.py            # 系统提示生成
├── command.py           # 斜杠命令系统
├── context.py           # 上下文加载（CLAUDE.md）
├── output.py            # 输出格式化工具
├── singleton.py         # 单例工具
├── tui.py               # Textual TUI 应用
└── ui_textual.py        # Textual UI 实现
```

## 核心组件

### 1. Agent 核心循环 (`agent.py`)

Agent 实现了经典的**工具调用循环模式**：

```python
while True:
    # 1. 调用模型
    response = client.messages.create(...)

    # 2. 检查是否有工具调用
    if response.stop_reason != "tool_use":
        return  # 任务完成

    # 3. 执行工具
    for tool_call in response.content:
        result = execute_tool(tool_call)
        results.append(result)

    # 4. 将结果添加到对话历史
    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": results})
```

**关键特性：**

- ✅ 线程安全的中断机制（`request_interrupt()`）
- ✅ 思考块显示（Thinking blocks）
- ✅ 子代理生成（`spawn_subagent()`）
- ✅ 任务管理集成（NAG 提醒）

### 2. 工具系统 (`tools.py`)

#### 工具定义

所有工具使用 dataclass 定义类型安全的输入模式：

```python
@dataclass
class BashToolCall:
    name: Literal["Bash"]
    command: str

@dataclass
class ReadToolCall:
    name: Literal["Read"]
    path: str
    limit: int | None = None
```

#### 工具分发

使用 match-case 进行类型安全的工具分发：

```python
def execute_tool(name: str, args: dict, ...) -> str:
    match name:
        case "Bash":
            tool = BashToolCall(...)
            return run_bash(tool.command, workdir)
        case "Read":
            tool = ReadToolCall(...)
            return run_read(tool.path, workdir, tool.limit)
        # ... 更多工具
```

#### 安全特性

- **路径安全**：`safe_path()` 确保文件访问不逃逸工作目录
- **命令安全**：`run_bash()` 阻止危险命令（`rm -rf /`、`sudo` 等）
- **输出截断**：所有工具输出限制在 50KB 以内

### 3. 技能系统 (`skill.py`)

三层加载架构：

```bash
Layer 1: 技能描述（系统提示中）
  - name: frontend-design
  - description: Create distinctive web interfaces
  - ~100 tokens per skill

Layer 2: 技能内容（调用 Skill 工具时）
  - 完整的 SKILL.md body
  - 详细指令和说明

Layer 3: 资源提示
  - scripts/: 可用脚本
  - references/: 参考文档
  - examples/: 示例代码
```

**技能加载流程：**

1. 启动时扫描 `.claude/skills/` 和 `~/.claude/plugins/`
2. 解析 SKILL.md 的 YAML frontmatter
3. 在系统提示中仅包含描述（节省 token）
4. 调用 Skill 工具时才加载完整内容

### 4. 任务管理 (`task.py`)

**约束规则：**

- ✅ 最多 20 个任务（防止无限列表）
- ✅ 同时只能有一个 `in_progress` 任务（强制专注）
- ✅ 每个任务必须有 `content`、`status`、`active_form`

**NAG 机制：**

```python
# 超过 10 轮没有 TaskUpdate
if task_manager.too_long_without_task():
    # 在消息前插入提醒
    results.insert(0, "<reminder>10+ turns without task update...")
```

**渲染格式：**

```bash
✔ 已完成任务
▣ 进行中任务 <- 正在做某事...
☐ 待处理任务

(1/3 completed)
```

### 5. 子代理系统 (`subagent.py`)

三种代理类型：

| 类型        | 工具权限   | 用途                   |
| ----------- | ---------- | ---------------------- |
| **Explore** | Bash、Read | 只读探索代码、查找文件 |
| **Plan**    | Bash、Read | 分析并生成实施计划     |
| **Code**    | 所有工具   | 实现功能和修复 bug     |

**子代理特性：**

- 📦 隔离的消息历史（不污染父代理）
- 🔄 不能递归生成子代理（防止无限嵌套）
- 📊 通过共享 UI 显示进度
- 🎯 仅返回最终文本摘要

### 6. 命令系统 (`command.py`)

使用装饰器注册命令：

```python
@command("/help", "Show available commands")
def cmd_help(ctx: ICommandContext) -> CommandResult:
    # ...
    return "continue"  # | "exit" | "clear"
```

**可用命令：**

- `/help` - 显示帮助
- `/exit` - 退出程序（或 ctrl+w）
- `/clear` - 清除对话历史
- `/skills` - 列出已加载技能
- `/config` - 显示配置信息

### 7. UI 抽象 (`interfaces.py` + `ui_textual.py`)

#### IAgentUI Protocol

```python
@runtime_checkable
class IAgentUI(Protocol):
    # 基础输出
    def text(self, message: object) -> None: ...
    def newline(self) -> None: ...
    def clear(self) -> None: ...

    # 样式输出
    def primary(self, message: str | None) -> None: ...
    def accent(self, message: str | None) -> None: ...
    def error(self, message: str | None) -> None: ...
    def debug(self, message: str | None) -> None: ...

    # Agent 特定输出
    def thinking(self, content: str, duration: float) -> None: ...
    def response(self, text: str) -> None: ...
    def tool_call(self, name: str, tool_input: dict) -> None: ...
    def tool_result(self, output: str, max_length: int) -> None: ...
```

#### TextualOutput 实现

通过回调函数解耦与 TUI 应用的直接依赖：

```python
class TextualOutput:
    def __init__(
        self,
        get_chat_log: Callable[[], RichLog],
        get_status_bar: Callable[[], Static],
        get_thinking_log: Callable[[], RichLog],
        store_thinking: Callable[[Text], None],
        is_thinking_view: Callable[[], bool],
    ) -> None:
        # ...
```

这允许单元测试时轻松 mock UI。

### 8. 配置管理 (`config.py`)

**配置优先级：**

```md
1. ~/.claude/settings.json 的 env 字段
2. 环境变量
3. 默认值
```

**支持的配置项：**

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-ant-...",
    "ANTHROPIC_BASE_URL": "https://api.anthropic.com",
    "ANTHROPIC_MODEL": "claude-opus-4-5-20251101",
    "MAX_THINKING_TOKENS": "31999"
  }
}
```

## 设计模式

### 1. 依赖注入模式

所有组件通过构造函数接收依赖：

```python
class Agent:
    def __init__(
        self,
        ui: IAgentUI,
        config: AgentConfig,
        system_prompt: str,
        tools: list[ToolParam],
        skill_loader: SkillLoader,
        task_manager: TaskManager,
    ) -> None:
        # ...
```

### 2. Strategy 模式

不同工具类型有不同的执行策略：

```python
# 策略 1: 同步执行
run_bash(command, workdir)

# 策略 2: 文件操作
run_read(path, workdir)

# 策略 3: 网络请求
run_web_search(query)
```

### 3. Template Method 模式

Agent 循环定义了算法骨架，子步骤可定制：

```python
def _agent_loop(self):
    while True:
        response = self._call_model()  # 步骤 1
        if self._should_stop(response):
            break
        results = self._execute_tools(response.content)  # 步骤 2
        self._update_history(results)  # 步骤 3
```

### 4. Observer 模式

UI 通过回调观察 Agent 状态：

```python
self.call_from_thread(self.output.status, "Thinking...")
```

## 线程安全

### 中断机制

使用 `threading.Lock` 保护中断标志：

```python
class Agent:
    def __init__(self):
        self._interrupt_lock = threading.Lock()
        self._interrupt_requested = False

    def request_interrupt(self) -> None:
        with self._interrupt_lock:
            self._interrupt_requested = True

    def _is_interrupt_requested(self) -> bool:
        with self._interrupt_lock:
            return self._interrupt_requested
```

### Agent 循环中的中断检查

```python
while True:
    if self._is_interrupt_requested():
        raise KeyboardInterrupt

    response = self.client.messages.create(...)

    if self._is_interrupt_requested():
        raise KeyboardInterrupt
```

## 扩展指南

### 添加新工具

1. 在 `tools.py` 定义 dataclass：

```python
@dataclass
class MyToolCall:
    name: Literal["MyTool"]
    param: str
```

2. 在 `BASE_TOOLS` 添加定义：

```python
{
    "name": "MyTool",
    "description": "...",
    "input_schema": {...}
}
```

3. 在 `execute_tool()` 添加 case：

```python
case "MyTool":
    return run_my_tool(tool.param, workdir)
```

### 添加新子代理类型

在 `subagent.py` 的 `AGENTS` 字典添加：

```python
AGENTS["Review"] = {
    "description": "Code review agent",
    "tools": ["Bash", "Read", "Grep"],
    "prompt": "You are a code reviewer...",
}
```

### 添加新命令

在 `command.py` 使用装饰器：

```python
@command("/mycommand", "Description")
def cmd_mycommand(ctx: ICommandContext) -> CommandResult:
    # 实现逻辑
    return "continue"
```

## 性能优化

1. **技能按需加载** - 仅在调用时加载完整内容
2. **输出截断** - 所有限制在 50KB
3. **LRU 缓存** - WebReader 使用 15 分钟缓存
4. **UI 缓存** - RichLog widget 缓存引用
5. **目录排除** - Glob/Grep 排除 node_modules 等

## 测试策略

项目使用 pytest 进行单元测试，覆盖：

- ✅ 工具执行逻辑
- ✅ 任务管理验证
- ✅ 技能加载和解析
- ✅ 命令处理
- ✅ 子代理生成

运行测试：

```bash
cd packages/agent-cli
uv run pytest
```

## 总结

Agent-CLI 是一个设计良好的 AI 代理框架，具有以下优点：

1. **清晰的架构** - 模块职责明确，依赖关系清晰
2. **类型安全** - 完整的类型注解和 dataclass
3. **可扩展性** - 工具、技能、子代理都易于扩展
4. **线程安全** - 支持中断和并发操作
5. **良好的测试** - 单元测试覆盖核心逻辑

该项目展示了如何使用现代 Python 特性（Protocol、TypeVar、dataclass、match-case）构建复杂的应用程序。
