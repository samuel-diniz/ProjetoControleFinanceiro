import time
from datetime import date
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from database.models import criar_tabelas
from services.finance import registrar_entrada, registrar_gasto
from services.resumo import gerar_resumo_mensal, obter_saldo_mensal
from services.dashboard import mostrar_dashboard
from utils.ui import sucesso, erro, aviso, titulo

console = Console()


def menu_principal():
    console.print(
        Panel.fit(
            "[bold cyan]CONTROLE FINANCEIRO[/bold cyan]\n"
            "[1] Registrar entrada\n"
            "[2] Registrar gasto\n"
            "[3] Atualizar resumo mensal\n"
            "[4] Ver saldo do mês atual\n"
            "[5] Dashboard do mês atual\n"
            "[0] Sair",
            border_style="cyan"
        )
    )
    return Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "0"])


def ver_saldo_atual():
    hoje = date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    saldo = obter_saldo_mensal(mes_atual, ano_atual)

    if saldo is not None:
        print(f'\nSaldo de {mes_atual:02d}/{ano_atual}: R${saldo:.2f}')
    else:
        print(f'Nenhum registro encontrado para {mes_atual:02d}/{ano_atual}')


def main():
    criar_tabelas()
    
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            registrar_entrada()
        
        elif opcao == '2':
            registrar_gasto()
        
        elif opcao == '3':
            with console.status("[bold green]Atualizando resumo mensal...[/bold green]"):
                time.sleep(0.6)
            gerar_resumo_mensal()

            sucesso('RESUMO MENSAL ATUALIZADO!')

        elif opcao == '4':
            with console.status("[bold green]Consultando saldo disponível...[/bold green]"):
                time.sleep(0.6)
            ver_saldo_atual()

            sucesso('SALDO ATUALIZADO!')
        
        elif opcao == '5':
            with console.status("[bold green]Carregando dashboard...[/bold green]"):
                time.sleep(0.4)
            mostrar_dashboard()
        
        elif opcao == '0':
            aviso('ENCERRANDO O PROGRAMA.')
            break
        
        else:
            erro('Opção Inválida. Por favor escolha uma opção válida.')

if __name__ == "__main__":
    main()