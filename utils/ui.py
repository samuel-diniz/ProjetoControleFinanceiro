from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.align import Align
from rich.text import Text

console = Console()

def sucesso(msg):
    console.print(Panel.fit(f"[bold green]✔ {msg}[/bold green]", border_style="green"))


def erro(msg):
    console.print(Panel.fit(f"[bold red]✖ {msg}[/bold red]", border_style="red"))


def aviso(msg):
    console.print(Panel.fit(f"[bold yellow]⚠ {msg}[/bold yellow]", border_style="yellow"))


def titulo(msg):
    console.print(f"\n[bold cyan]{msg}[/bold cyan]")


def mostrar_saldo(saldo):
    cor = 'green' if saldo >= 0 else 'red'
    sinal = '' if saldo >= 0 else '-'
    console.print(
        Panel.fit(
            f"[bold {cor}]Saldo Atual: R$ {abs(saldo):.2f}[/bold {cor}]",
            border_style=cor
        )
    )


def loading(msg="Processando..."):
    return console.status(f"[bold green]{msg}[/bold green]")