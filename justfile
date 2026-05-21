# Python recipes

python-install:
    uv tool install --editable packages/agent-cli

python-dev:
    uv run packages/agent-cli/src/agent_cli/lang_graph.py

python-dev-agent-cli:
    uv run agent-cli

python-dev-nano-gpt:
    ./packages/nano-gpt/src/nano_gpt/data/input.sh && uv run nano-gpt

python-lint:
    uv run pyright && uv run ruff check

python-lint-fix:
    uv run ruff check --fix

python-test:
    uv run pytest

# Rust recipes

rust-build:
    cargo build --release

rust-deps:
    cargo install mdbook cargo-edit cargo-release cargo-workspace

rust-dev-basis:
    cargo run -p basis

rust-dev-rustlings:
    cd crates/rustlings && cargo run -- watch

rust-docs:
    mdbook build
    cargo doc --workspace --no-deps && mv target/doc book/

rust-docs-book:
    mdbook build

rust-docs-api:
    cargo doc --workspace --no-deps && mv target/doc book/

rust-e2e:
    cargo run -p basis --release
    cd crates/rustlings && cargo run --release -- verify

rust-format:
    cargo fmt && cargo clippy --fix --allow-dirty --allow-staged

rust-lint:
    cargo fmt --check && cargo clippy --all-targets --release --locked -- -D clippy::all

rust-release:
    cargo release -x

rust-test:
    cargo test
