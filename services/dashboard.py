from datetime import date
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from database.connection import get_connection
from utils.ui import console, mostrar_saldo, titulo, erro




def menu_dashboard():
    console.print(
        Panel.fit(
            "[bold cyan]DASHBOARD[/bold cyan]\n"
            "[1] Ver mês específico\n"
            "[2] Comparar meses\n"
            "[3] Top categorias de gastos\n"
            "[4] Maior gasto do período\n"
            "[0] Voltar",
            border_style="cyan"
        )
    )
    return Prompt.ask("Escolha: ", choices=["1", "2", "3", "4", "0"])


def obter_totais(mes, ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM entradas
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    entradas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    gastos = cursor.fetchone()[0]


    conn.close()
    return entradas, gastos


def ver_mes_especifico():
    mes = int(Prompt.ask('Mês (1-12)'))
    ano = int(Prompt.ask('Ano'))

    entradas, gastos = obter_totais(mes, ano)
    saldo = entradas - gastos

    titulo(f'MÊS {mes:02d}/{ano}')

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("Entradas", justify="right", style="green")
    tabela.add_column("Gastos", justify="right", style="red")

    tabela.add_row(
        f"R$ {entradas:.2f}",
        f"R$ {gastos:.2f}")

    console.print(tabela)
    mostrar_saldo(saldo)


def comparar_meses():
    console.print("\n[bold]Primeiro período[/bold]")
    mes1 = int(Prompt.ask('Mês'))
    ano1 = int(Prompt.ask('Ano'))

    console.print("\n[bold]Segundo período[/bold]")
    mes2 = int(Prompt.ask('Mês'))
    ano2 = int(Prompt.ask('Ano'))

    e1, g1 = obter_totais(mes1, ano1)
    e2, g2 = obter_totais(mes2, ano2)

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("Periodo")
    tabela.add_column("Entradas", justify="right", style="green")
    tabela.add_column("Gastos", justify="right", style="red")
    tabela.add_column("Saldo", justify="right", style="cyan")

    tabela.add_row(f"{mes1:02d}/{ano1}", f"R$ {e1:.2f}", f"R$ {g1:.2f}", f"R$ {e1 - g1:.2f}")
    tabela.add_row(f"{mes2:02d}/{ano2}", f"R$ {e2:.2f}", f"R$ {g2:.2f}", f"R$ {e2 - g2:.2f}")

    console.print(tabela)


def top_categorias():
    mes = int(Prompt.ask('Mês'))
    ano = int(Prompt.ask('Ano'))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT categoria, SUM(valor) as total
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
        GROUP BY categoria
        ORDER BY total DESC
    """, (f"{mes:02d}", str(ano)))

    rows = cursor.fetchall()
    conn.close()

    tabela = Table(box=box.ROUNDED)
    tabela.add_column("Categoria")
    tabela.add_column("Total", justify="right", style="red")

    for row in rows:
        tabela.add_row(row[0], f"R$ {row[1]:.2f}")

    console.print(tabela)


def maior_gasto():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT descricao, valor, data
        FROM gastos
        ORDER BY valor DESC
        LIMIT 1
    """)


    row = cursor.fetchone()
    conn.close()

    if row:
        titulo("MAIOR GASTO REGISTRADO")
        console.print(f"[red]{row[0]}[/red]")
        console.print(f"Valor: R$ {row[1]:.2f}")
        console.print(f"Data: {row[2]}")
    else:
        console.print("[yellow]Nenhum gasto encontrado[/yellow]")

 
def mostrar_dashboard():
    while True:
        opcao = menu_dashboard()

        if opcao == '1':
            ver_mes_especifico()
        
        elif opcao == '2':
            comparar_meses()
        
        elif opcao == '3':
            top_categorias()
        
        elif opcao == '4':
            maior_gasto()

        elif opcao == '0':
            break
        
        else: 
            erro("Opção inválida. Escolha uma opção válida")