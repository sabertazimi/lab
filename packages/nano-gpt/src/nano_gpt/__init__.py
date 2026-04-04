from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor

DATA_DIR = Path(str(files("nano_gpt") / "data"))


@dataclass
class GPTConfig:
    batch_size: int = 64
    block_size: int = 256
    max_iters: int = 5000
    eval_interval: int = 500
    learning_rate: float = 3e-4
    eval_iters: int = 200
    n_embd: int = 384
    n_head: int = 6
    n_layer: int = 6
    dropout: float = 0.2

    @property
    def head_size(self) -> int:
        return self.n_embd // self.n_head

    @property
    def device(self) -> torch.device:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def encode(stoi: dict[str, int], string: str) -> list[int]:
    return [stoi[char] for char in string]


def decode(itos: dict[int, str], indices: list[int]) -> str:
    return "".join([itos[item] for item in indices])


def get_batch(
    data: Tensor,
    batch_size: int = 64,
    block_size: int = 256,
    device: torch.device | None = None,
) -> tuple[Tensor, Tensor]:
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i : i + block_size] for i in ix])
    y = torch.stack([data[i + 1 : i + block_size + 1] for i in ix])
    if device is not None:
        x, y = x.to(device), y.to(device)
    return x, y


@torch.no_grad()
def estimate_loss(
    model: GPTLanguageModel,
    train_data: Tensor,
    val_data: Tensor,
    config: GPTConfig,
) -> dict[str, float]:
    out: dict[str, float] = {}
    model.eval()
    for split, data in [("train", train_data), ("val", val_data)]:
        losses = torch.zeros(config.eval_iters)
        for k in range(config.eval_iters):
            x, y = get_batch(data, config.batch_size, config.block_size, config.device)
            _, loss = model(x, y)
            losses[k] = loss.item()
        out[split] = losses.mean().item()
    model.train()
    return out


class Head(nn.Module):
    def __init__(self, n_embd: int, head_size: int, block_size: int, dropout: float):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: Tensor) -> Tensor:
        _b, t, _ = x.shape
        k = self.key(x)
        q = self.query(x)
        wei = q @ k.transpose(-2, -1) * k.shape[-1] ** -0.5
        wei = wei.masked_fill(self.tril[:t, :t] == 0, float("-inf"))  # pyright: ignore[reportIndexIssue]
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)
        v = self.value(x)
        return wei @ v


class MultiHeadAttention(nn.Module):
    def __init__(
        self, n_embd: int, n_head: int, head_size: int, block_size: int, dropout: float
    ):
        super().__init__()
        self.heads = nn.ModuleList(
            [Head(n_embd, head_size, block_size, dropout) for _ in range(n_head)]
        )
        self.proj = nn.Linear(head_size * n_head, n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: Tensor) -> Tensor:
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        return self.dropout(self.proj(out))


class FeedForward(nn.Module):
    def __init__(self, n_embd: int, dropout: float):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout),
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.net(x)


class Block(nn.Module):
    def __init__(self, n_embd: int, n_head: int, block_size: int, dropout: float):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_embd, n_head, head_size, block_size, dropout)
        self.ffwd = FeedForward(n_embd, dropout)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x: Tensor) -> Tensor:
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x


class GPTLanguageModel(nn.Module):
    def __init__(self, vocab_size: int, config: GPTConfig):
        super().__init__()
        self.config = config
        self.token_embedding_table = nn.Embedding(vocab_size, config.n_embd)
        self.position_embedding_table = nn.Embedding(config.block_size, config.n_embd)
        self.blocks = nn.Sequential(
            *[
                Block(config.n_embd, config.n_head, config.block_size, config.dropout)
                for _ in range(config.n_layer)
            ]
        )
        self.ln_f = nn.LayerNorm(config.n_embd)
        self.lm_head = nn.Linear(config.n_embd, vocab_size)
        self.apply(self._init_weights)

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:  # pyright: ignore[reportUnnecessaryComparison]
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(
        self, idx: Tensor, targets: Tensor | None = None
    ) -> tuple[Tensor, Tensor | None]:
        b, t = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(
            torch.arange(t, device=self.config.device)
        )
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            return logits, None

        b, t, c = logits.shape
        loss = F.cross_entropy(logits.view(b * t, c), targets.view(b * t))
        return logits, loss

    def generate(self, idx: Tensor, max_new_tokens: int) -> Tensor:
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -self.config.block_size :]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx


def main() -> None:
    torch.manual_seed(1337)  # pyright: ignore[reportUnknownMemberType]

    config = GPTConfig()

    with open(DATA_DIR / "input.txt", encoding="utf-8") as f:
        text = f.read()

    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    stoi: dict[str, int] = {ch: i for i, ch in enumerate(chars)}
    itos: dict[int, str] = {i: ch for i, ch in enumerate(chars)}

    data = torch.tensor(encode(stoi, text), dtype=torch.long)
    n = int(0.9 * len(data))
    train_data = data[:n]
    val_data = data[n:]

    model = GPTLanguageModel(vocab_size, config).to(config.device)
    print(sum(p.numel() for p in model.parameters()) / 1e6, "M parameters")

    optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate)

    for iter in range(config.max_iters):
        if iter % config.eval_interval == 0 or iter == config.max_iters - 1:
            losses = estimate_loss(model, train_data, val_data, config)
            print(
                f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}"
            )

        xb, yb = get_batch(
            train_data, config.batch_size, config.block_size, config.device
        )
        _, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()  # pyright: ignore[reportUnknownMemberType]

    context = torch.zeros((1, 1), dtype=torch.long, device=config.device)
    print(decode(itos, model.generate(context, max_new_tokens=500)[0].tolist()))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
