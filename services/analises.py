from rich.panel import Panel
from rich.prompt import Prompt
from utils.ui import console
from services.charts import grafico_gastos_mensais, evolucao_saldo
from services.report_excel import exportar_excel
from services.report_pdf import exportar_pdf
from services.resumo import ranking_anual
from utils.validators import validar_mes, validar_ano


def menu_analises():
    while True:
        console.print(
            Panel.fit(
                "[bold cyan]ANÁLISES & RELATÓRIOS[/bold cyan]\n"
                "[1] Gráfico de gastos mensais\n"
                "[2] Evolução de saldo\n"
                "[3] Exportar relatório em PDF\n"
                "[4] Exportar relatório em Excel\n"
                "[5] Ranking anual de categorias\n"
                "[0] Voltar",
                border_style="cyan"
            )
        )

        opcao = Prompt.ask("Escolha", choices=["1","2","3","4","5","0"])

        if opcao == "1":
            mes = None
            while mes is None:
                mes = validar_mes()

            ano = None
            while ano is None:
                ano = validar_ano()

            grafico_gastos_mensais(mes, ano)

        elif opcao == "2":
            ano = None
            while ano is None:
                ano = validar_ano()

            evolucao_saldo(ano)

        elif opcao == "3":
            ano = None
            while ano is None:
                ano = validar_ano()

            exportar_pdf(ano)

        elif opcao == "4":
            ano = None
            while ano is None:
                ano = validar_ano()

            exportar_excel(ano)

        elif opcao == "5":
            ano = None
            while ano is None:
                ano = validar_ano()
                
            ranking_anual(ano)

        elif opcao == "0":
            break
