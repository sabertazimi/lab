# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.4.0](https://github.com/sabertazimi/lab/compare/v3.3.0...v3.4.0) (2026-06-08)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#1001](https://github.com/sabertazimi/lab/issues/1001)) ([6c6e250](https://github.com/sabertazimi/lab/commit/6c6e2509c9c6529d88c8a2c8e2dded6092d959bd))
- **deps:** update dependencies (non-major) ([#1006](https://github.com/sabertazimi/lab/issues/1006)) ([9e181ab](https://github.com/sabertazimi/lab/commit/9e181ab9433b3246779710d9f19409e260aa72a0))
- **deps:** update dependencies (non-major) ([#1011](https://github.com/sabertazimi/lab/issues/1011)) ([42d5719](https://github.com/sabertazimi/lab/commit/42d5719c9f41ad0b5263b61fda54d8166861cd55))
- **deps:** update dependencies (non-major) ([#989](https://github.com/sabertazimi/lab/issues/989)) ([339330b](https://github.com/sabertazimi/lab/commit/339330b72dd6a34848ab0c043a385e6fd847f02b))
- **deps:** update dependency pydantic to >=2.13.4 ([#1010](https://github.com/sabertazimi/lab/issues/1010)) ([ae0aa2f](https://github.com/sabertazimi/lab/commit/ae0aa2fe51c914c4490d33cbe8756c47a778634a))
- **deps:** update dependency rich to >=15.0.0 ([#991](https://github.com/sabertazimi/lab/issues/991)) ([f4ac3a3](https://github.com/sabertazimi/lab/commit/f4ac3a31146e7c5662329bd573dde8f2834102b6))

### Features

- **agent:** add `LangGraph` `ReAct` agent demo with tool calling ([f5a9841](https://github.com/sabertazimi/lab/commit/f5a9841a53acef28f8bde7e9c1f1f1c185d63e46))

# [3.3.0](https://github.com/sabertazimi/lab/compare/v3.2.0...v3.3.0) (2026-04-04)

### Bug Fixes

- **agent-skills:** avoid duplicate headers in skill content ([ad9ed27](https://github.com/sabertazimi/lab/commit/ad9ed27100bc7c8bbd1d635b81be593f135804a3))
- **deps:** update dependencies (non-major) ([#968](https://github.com/sabertazimi/lab/issues/968)) ([996e387](https://github.com/sabertazimi/lab/commit/996e38713364c1f42b4db35e752d2196d77d168a))
- **deps:** update dependencies (non-major) ([#972](https://github.com/sabertazimi/lab/issues/972)) ([08ed245](https://github.com/sabertazimi/lab/commit/08ed245faeea1435b424e76b7ceae3cd45d219f2))
- **deps:** update dependencies (non-major) ([#980](https://github.com/sabertazimi/lab/issues/980)) ([cde33db](https://github.com/sabertazimi/lab/commit/cde33db75ad1eecd874d3684019322287d1e22b5))
- **deps:** update dependency textual to v8 ([#971](https://github.com/sabertazimi/lab/issues/971)) ([3095cb3](https://github.com/sabertazimi/lab/commit/3095cb3976974a28b5a0ab27a2791a626f5b56ea))

### Features

- **agent-cli:** enhance CLI with headless mode and UI improvements ([#966](https://github.com/sabertazimi/lab/issues/966)) ([32ef88c](https://github.com/sabertazimi/lab/commit/32ef88c8589dff5ad92dc7512ff508444e3a394d))
- **agent-thinking:** implement thinking mode ([798dcc0](https://github.com/sabertazimi/lab/commit/798dcc038de001e58635a190d61b22c49acdbad8))
- **agent:** add command autocomplete to TUI input ([#961](https://github.com/sabertazimi/lab/issues/961)) ([dca7f08](https://github.com/sabertazimi/lab/commit/dca7f089b16497948dbec0d95ef058dd559118f0))
- **agent:** add spinner animation to status bar ([#964](https://github.com/sabertazimi/lab/issues/964)) ([5c8ae65](https://github.com/sabertazimi/lab/commit/5c8ae65917792efbf3db6f3026cc934113314cec))
- **ai-gpt:** add nanoGPT package for building GPT from scratch ([#988](https://github.com/sabertazimi/lab/issues/988)) ([cdd87c2](https://github.com/sabertazimi/lab/commit/cdd87c23bd244a0ee432f6710d1c7dba2003ca8d))

### Performance Improvements

- **agent-tools:** optimize Glob and Grep with directory exclusions ([931825c](https://github.com/sabertazimi/lab/commit/931825cf24f8e0d7e10d02fefcbdc0b3be62498f))

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

### Bug Fixes

- **agent-cli:** correct f-string syntax and enhance agent status display ([#955](https://github.com/sabertazimi/lab/issues/955)) ([2e83e43](https://github.com/sabertazimi/lab/commit/2e83e4332ae5e75f383b2086affef65ded70d9ad))
- **agent-cli:** remove unused `/tasks` command ([2ada3a6](https://github.com/sabertazimi/lab/commit/2ada3a61dabef662cd3612c4a64cdaa7e52df050))

### Features

- **agent-cli:** add config file support ([#953](https://github.com/sabertazimi/lab/issues/953)) ([d16e75c](https://github.com/sabertazimi/lab/commit/d16e75ce50eab2df3eac720b4ea21a8d609857b3))
- **agent-cli:** add graceful Ctrl+C interruption handling ([#956](https://github.com/sabertazimi/lab/issues/956)) ([9386b8f](https://github.com/sabertazimi/lab/commit/9386b8fb037d2e603de5aca923a1d230423c184d))
- **agent-cli:** add slash command system with interactive commands ([#957](https://github.com/sabertazimi/lab/issues/957)) ([faafe13](https://github.com/sabertazimi/lab/commit/faafe13bcbd9f2dd8dc568bd67ef3956c33c31fb))
- **agent-skills:** add Claude Code Plugins integration ([#954](https://github.com/sabertazimi/lab/issues/954)) ([1b73de4](https://github.com/sabertazimi/lab/commit/1b73de4e166b4ac3a5ca682bc5f6e9f355a0e779))
- **agent-tools:** add Glob, Grep, WebSearch, and WebReader tools ([#959](https://github.com/sabertazimi/lab/issues/959)) ([3776f3a](https://github.com/sabertazimi/lab/commit/3776f3af039316a3e090be43a11ad0c199cbfcef))
- **agent-tui:** add Textual TUI with interrupt support ([#958](https://github.com/sabertazimi/lab/issues/958)) ([d51cae3](https://github.com/sabertazimi/lab/commit/d51cae3523a9acdd296aad4b1bdce0258d65dc28))
- **agent:** add creator and email information ([#952](https://github.com/sabertazimi/lab/issues/952)) ([b64d99c](https://github.com/sabertazimi/lab/commit/b64d99c1cef73c68e9121c841d637fef414992a7))

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

### Bug Fixes

- **agent:** add cyber agent identity and normalize line endings ([2ebed0c](https://github.com/sabertazimi/lab/commit/2ebed0c322d9f708ffa14b50cd8c08bc2f028972))

### Features

- **agent-cli:** integrate rich library for terminal output formatting ([#947](https://github.com/sabertazimi/lab/issues/947)) ([6291def](https://github.com/sabertazimi/lab/commit/6291def694fd04a338c95a4419955b0d1a0c9a96))
- **agent-context:** add CLAUDE.md system reminder support ([#946](https://github.com/sabertazimi/lab/issues/946)) ([d4ea0b2](https://github.com/sabertazimi/lab/commit/d4ea0b291b33fdb4cf6885ab0f5b73aa845122a5))
- **agent-skills:** add skill system with SkillLoader ([#950](https://github.com/sabertazimi/lab/issues/950)) ([3f4668e](https://github.com/sabertazimi/lab/commit/3f4668e4c7e4d446ebbd82ca4f2a69627f4ae50f))
- **agent-subagent:** add subagent architecture with Task tool ([#949](https://github.com/sabertazimi/lab/issues/949)) ([11115d1](https://github.com/sabertazimi/lab/commit/11115d1a733e3db98be8944f94d1c4d30e58d394))
- **agent-task:** add task tracking system with TaskManager singleton ([#945](https://github.com/sabertazimi/lab/issues/945)) ([3300927](https://github.com/sabertazimi/lab/commit/330092705459feaa817cfe6156f85f195b4cde64))
- **agent-tools:** improve Windows compatibility for bash tool ([#948](https://github.com/sabertazimi/lab/issues/948)) ([e9185ef](https://github.com/sabertazimi/lab/commit/e9185efb7317da1684893a1faad2004b1fe56f87))
- **agent:** add branding banner and custom semantic theme ([#951](https://github.com/sabertazimi/lab/issues/951)) ([a462230](https://github.com/sabertazimi/lab/commit/a4622308a7bff307ba5eceb4b194a32c8c0010d6))
- **agent:** implement agent loop and tool call ([#943](https://github.com/sabertazimi/lab/issues/943)) ([155e452](https://github.com/sabertazimi/lab/commit/155e452237bb22106aea1b147f7b66c13c86a017))
- **pnpm:** add python and rust packages to pnpm workspace ([#944](https://github.com/sabertazimi/lab/issues/944)) ([4be9748](https://github.com/sabertazimi/lab/commit/4be97484e842bb72ea65894f99e495ce08c3edc7))
- **python-type:** setup type hint static check ([#942](https://github.com/sabertazimi/lab/issues/942)) ([e0e1a2c](https://github.com/sabertazimi/lab/commit/e0e1a2cbb8d53ed482eec2ab30e8aa94cdeefc65))
