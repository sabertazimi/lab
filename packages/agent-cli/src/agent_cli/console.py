from rich.console import Console
from rich.theme import Theme

console = Console(
    theme=Theme(
        {
            "primary": "green",
            "accent": "grey62",
            "muted": "bright_black",
            "error": "red",
        }
    )
)
