from rich.console import Console
from rich.panel import Panel

console = Console()

def sucesso(msg):
    console.print(Panel.fit(f"[bold green]✔ {msg}[/bold green]", border_style="green"))

def erro(msg):
    console.print(Panel.fit(f"[bold red]✖ {msg}[/bold red]", border_style="red"))

def aviso(msg):
    console.print(Panel.fit(f"[bold yellow]⚠ {msg}[/bold yellow]", border_style="yellow"))