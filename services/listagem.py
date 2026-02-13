from rich.table import Table
from rich import box
from database.repository import listar_entradas, listar_gastos
from utils.ui import console, titulo, aviso


def mostrar_entradas():
    rows = listar_entradas()

    if not rows:
        aviso('Nenhuma entrada cadastrada.')
        return
    
    titulo("ENTRADAS")

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("ID", justify="right", style="cyan", width=6)
    tabela.add_column("Data")
    tabela.add_column("Descrição")
    tabela.add_column("Categoria")
    tabela.add_column("Valor", justify="right", style="green")

    for row in rows:
        tabela.add_row(
            str(row["id"]),
            str(row["data"]),
            row["descricao"],
            row["categoria"],
            f"R$ {row['valor']:.2f}"
        )
    
    console.print(tabela)


def mostrar_gastos():
    rows = listar_gastos()

    if not rows:
        aviso('Nenhum gasto cadastrado.')
        return
    
    titulo("GASTOS")

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("ID", justify="right", style="cyan", width=6)
    tabela.add_column("Data")
    tabela.add_column("Descrição")
    tabela.add_column("Categoria")
    tabela.add_column("Forma")
    tabela.add_column("Valor", justify="right", style="red")

    for row in rows:
        tabela.add_row(
            str(row["id"]),
            str(row["data"]),
            row["descricao"],
            row["categoria"],
            row["forma_pagamento"],
            f"R$ {row['valor']:.2f}"
        )
    
    console.print(tabela)