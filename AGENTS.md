# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## Project Overview

Lab is a polyglot monorepo with Web apps, Python packages, and Rust crates.

**Stack**: pnpm + uv + Cargo workspaces | React + Vite + TypeScript + Tailwind | Vue 3 | Python | Rust
**Packages**: 9 web packages, 1+ Python packages, 3+ Rust crates

## Common Commands

```bash
# Web
pnpm web:build        # Build all to dist/
pnpm web:lint         # ESLint + Stylelint + TypeScript
pnpm web:dev          # Start portfolio (default)

# Python
pnpm python:dev       # Run agent-cli
pnpm python:lint      # pyright + ruff
pnpm python:test      # pytest

# Rust
pnpm rust:build       # Cargo build --release
pnpm rust:lint        # rustfmt + clippy
pnpm rust:test        # cargo test
```

**IMPORTANT**: Always use `pnpm` over `npm`, use `uv` over `pip`.

## Architecture

**Web (packages/)**: `dblp`, `m-league-reviewer`, `react-renderer`, `mortal-ui`, `vue-design`, `vue-trello`, `echarts-dashboard`, `vue-challenges`, `portfolio`

**Python (packages/)**: `agent-cli` (Claude Code minimal implementation)

**Rust (crates/)**: `basis`, `rustlings`, `exercism/*`

## Common Patterns

- **Shadcn UI**: `pnpm dlx shadcn@latest add [component]` - Never modify `src/components/ui/`
- **State**: Zustand (`src/stores/`), Redux (`src/store/`), Pinia (`src/store/`)
- **Styling**: Tailwind CSS + `class-variance-authority` + `clsx` + `tailwind-merge`
- **Testing**: Vitest + Playwright | `*.test.ts`, `*.spec.ts`

## Key Files

- `pnpm-workspace.yaml` - pnpm workspace (web + rust + python)
- `pyproject.toml` - uv workspace config
- `Cargo.toml` - Cargo workspace config
- `tsconfig.json` - TypeScript strict mode, `@/*` aliases
- `eslint.config.mjs` - ESLint flat config
- `.prettierrc.json` - Tailwind plugin, 80 cols, no semicolons

## Constraints

**Web**: pnpm only | Don't modify `src/components/ui/` | TypeScript strict | Don't commit `dist/`, `node_modules/`

**Python**: uv only | pyright strict | ruff required | Don't commit `.venv/`, `uv.lock`

**Rust**: cargo only | rustfmt + clippy required | Don't commit `target/`

## Commit Style

[Conventional Commits](https://www.conventionalcommits.org/): `<type>(<scope>): <description>`

Types: feat, fix, chore, docs, refactor, perf, test, build, ci, style

## Footer

DO NOT add Claude/Cursor (ANY agents) co-authorship footer to commits
