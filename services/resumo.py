from collections import defaultdict
from rich.table import Table
from rich.console import Console
from database.connection import get_connection
from database.repository import buscar_resumo_mensal

console = Console()


def gerar_resumo_mensal():
    entradas, gastos = buscar_resumo_mensal()

    resumo = defaultdict(lambda: {'entradas': 0, 'gastos': 0})

    for row in entradas:
        chave = (int(row['mes']), int(row['ano']))
        resumo[chave]['entradas'] = row['total'] or 0

    for row in gastos:
        chave = (int(row['mes']), int(row['ano']))
        resumo[chave]['gastos'] = row['total'] or 0

    tabela = Table(title="Resumo Mensal")

    tabela.add_column("Mês/Ano", style="cyan")
    tabela.add_column("Entradas", style="green")
    tabela.add_column("Gastos", style="red")
    tabela.add_column("Saldo", style="bold")

    for (mes, ano) in sorted(resumo.keys(), key=lambda x: (x[1], x[0])):
        entradas = resumo[(mes, ano)]['entradas']
        gastos = resumo[(mes, ano)]['gastos']
        saldo = entradas - gastos

        tabela.add_row(
            f"{mes:02d}/{ano}",
            f"R$ {entradas:.2f}",
            f"R$ {gastos:.2f}",
            f"R$ {saldo:.2f}",
        )

    console.print(tabela)



def obter_saldo_mensal(mes, ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(valor), 0)
        FROM entradas
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))

    total_entradas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            COALESCE(SUM(valor), 0)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))

    total_gastos = cursor.fetchone()[0]

    conn.close()

    return total_entradas - total_gastos