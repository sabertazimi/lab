# Agent CLI

Minimal Claude Code with `Bash`/`Read`/`Write`/`Edit` tools, task planning, subagent orchestration, and skill system support.

## Getting Started

```bash
uv tool install --editable .
ac # or `agent-cli`
```

## Configuration

Setup your configuration in `~/.claude/settings.json` or `.env`:

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_anthropic_api_key",
    "ANTHROPIC_BASE_URL": "https://api.anthropic.com",
    "ANTHROPIC_MODEL": "claude-opus-4-5-20251101"
  }
}
```

```bash
ANTHROPIC_AUTH_TOKEN="your_anthropic_api_key"
ANTHROPIC_BASE_URL="https://api.anthropic.com"
ANTHROPIC_MODEL="claude-opus-4-5-20251101"
```

## References

- [Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code)
