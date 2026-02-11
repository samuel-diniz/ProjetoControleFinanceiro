from datetime import date
from database.connection import get_connection
from rich.table import Table
from rich import box
from utils.ui import console, mostrar_saldo, titulo


def mostrar_dashboard():
    hoje = date.today()
    mes = hoje.month
    ano = hoje.year

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            COALESCE(SUM(valor), 0)
        FROM entradas
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    entradas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            COALESCE(SUM(valor), 0)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    gastos = cursor.fetchone()[0]


    conn.close()

    saldo = entradas - gastos

    titulo(f'DASHBOARD {mes:02d}/{ano}')

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("Entradas", justify="right", style="green")
    tabela.add_column("Gastos", justify="right", style="red")

    tabela.add_row(f"R$ {entradas:.2f}", f"{gastos:.2f}")

    console.print(tabela)
    mostrar_saldo(saldo)

