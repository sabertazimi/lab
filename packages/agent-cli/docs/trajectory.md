# Agent-CLI Trajectory

## 启动测试

```bash
pnpm python:dev
```

**验证项：**

- [ ] 显示渐变色 ASCII Art Banner（cyan → blue → magenta）
- [ ] 显示 Model 和 Workdir 信息
- [ ] 显示 "Type '/help' to see available commands."
- [ ] 输入框获得焦点，placeholder 显示正确

## 1. 斜杠命令测试

| 命令                | 预期结果                              |
| ------------------- | ------------------------------------- |
| `/help`             | 显示所有可用命令列表                  |
| `/config`           | 显示当前 Model 和 Workdir             |
| `/skills`           | 列出已加载的技能（名称 + token 估算） |
| `/clear`            | 清空对话历史，重新显示 banner         |
| `/exit` 或 `ctrl+w` | 退出程序                              |

**命令补全测试：**

- [ ] 输入 `/` 后显示命令下拉列表（向上弹出）
- [ ] 选择补全项后正确填充

## 2. 基础工具测试

依次输入以下提示词：

### 2.1 Bash 工具

```md
运行命令 echo "Hello from agent-cli"
```

**验证：** 显示 `● Bash(echo "Hello from agent-cli")` 和输出

### 2.2 Read 工具

```md
读取 CLAUDE.md 文件的内容
```

**验证：** 显示 `● Read(CLAUDE.md)` 和文件预览

### 2.3 Write 工具

```md
创建一个新文件 test-output.txt，内容为 "Agent-CLI refactor test"
```

**验证：** 显示 `● Write(test-output.txt)` 和成功消息

### 2.4 Edit 工具

```md
将 test-output.txt 中的 "test" 替换为 "verification"
```

**验证：** 显示 `● Edit(test-output.txt)` 和编辑确认

### 2.5 Glob 工具

```md
查找所有 .py 文件在 packages/agent-cli/src 目录下
```

**验证：** 显示 `● Glob(*.py)` 和文件列表

### 2.6 Grep 工具

```md
在 packages/agent-cli/src 中搜索 "class Agent"
```

**验证：** 显示 `● Grep(class Agent)` 和匹配结果

## 3. Web 工具测试

### 3.1 WebSearch 工具

```md
搜索 "Python asyncio tutorial 2024"
```

**验证：** 显示 `● WebSearch(...)` 和搜索结果

### 3.2 WebReader 工具

```md
获取 https://docs.python.org/3/library/typing.html 的内容
```

**验证：** 显示 `● WebReader(...)` 和 markdown 内容预览

## 4. 任务管理测试

```md
创建一个任务列表来追踪以下工作：1. 阅读代码结构 2. 理解核心逻辑 3. 编写文档
```

**验证：**

- [ ] 显示 `● TaskUpdate(...)`
- [ ] 任务列表渲染：`☐` 待处理 / `▣` 进行中 / `✔` 已完成
- [ ] 显示进度 `(0/3 completed)`

## 5. Thinking 功能测试

发送一个需要深度思考的问题：

```md
分析 packages/agent-cli/src/agent_cli/agent_core.py 的设计模式和架构决策
```

**验证：**

- [ ] 显示 `● Thinking (x.xs)` 蓝色指示器
- [ ] 显示 "press ctrl+o to view details"
- [ ] 按 `ctrl+o` 切换到 Thinking 视图
- [ ] Thinking 视图显示完整思考内容（蓝色 bullet + dim 文本）
- [ ] 再按 `ctrl+o` 返回聊天视图

## 6. 子代理测试（如果支持）

```md
使用 Explore 代理搜索所有使用 IAgentUI 接口的文件
```

**验证：**

- [ ] 状态栏显示 "Preparing Explore agent..."
- [ ] 状态栏实时更新工具调用
- [ ] 完成后显示 "x tools used"
- [ ] 返回精简的结果摘要

## 7. 技能系统测试（如果有技能）

```md
列出可用的技能，然后加载其中一个
```

**验证：**

- [ ] `/skills` 显示已加载技能
- [ ] 调用 Skill 工具后显示 `<skill-loaded>` 内容

## 8. 中断测试

发送一个会触发多次工具调用的请求：

```md
分析 packages/agent-cli/src 下所有 Python 文件的结构
```

在执行过程中按 `ctrl+c`

**验证：**

- [ ] 状态栏显示 "Interrupting..."
- [ ] 显示 `⎿ Interrupted by user`
- [ ] Agent 返回中断确认和已完成工作摘要
- [ ] 可以继续输入新消息

## 9. 快捷键测试

| 快捷键   | 预期行为              |
| -------- | --------------------- |
| `ctrl+c` | 中断当前 agent loop   |
| `ctrl+l` | 清屏，重新显示 banner |
| `ctrl+o` | 切换 Thinking 视图    |
| `ctrl+w` | 退出程序              |
| `Enter`  | 提交消息              |

## 10. 错误处理测试

### 10.1 路径安全

```md
读取 ../../../etc/passwd 文件
```

**验证：** 返回 "Path escapes workspace" 错误

### 10.2 并发输入

在 agent 运行时尝试输入新消息
**验证：** 显示 "Agent is still running. Press ctrl+c to interrupt."

## 11. 清理

测试完成后：

```bash
# 删除测试文件
rm test-output.txt
```

## 测试检查清单

- [ ] Banner 正确显示
- [ ] 所有斜杠命令工作
- [ ] 命令补全正常
- [ ] Bash/Read/Write/Edit/Glob/Grep 工具正常
- [ ] WebSearch/WebReader 工具正常
- [ ] TaskUpdate 工具正常
- [ ] Thinking 显示和切换正常
- [ ] 中断机制正常
- [ ] 所有快捷键正常
- [ ] 错误处理正常
- [ ] 子代理功能正常（如支持）
- [ ] 技能系统正常（如有技能）
