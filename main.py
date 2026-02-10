from datetime import date
from database.models import criar_tabelas
from services.finance import registrar_entrada, registrar_gasto
from services.resumo import gerar_resumo_mensal, obter_saldo_mensal


def menu_principal():
    print('\n=== CONTROLE FINANCEIRO ===')
    print('1 - Registrar entrada')
    print('2 - Registrar gasto')
    print('3 - Atualizar resumo mensal')
    print('4 - Ver saldo do mês atual')
    print('0 - Sair')
    return input('Escolha uma opção: ').strip()


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
            gerar_resumo_mensal()
            print('RESUMO MENSAL ATUALIZADO!')
        
        elif opcao == '4':
            ver_saldo_atual()
        
        elif opcao == '0':
            print('ENCERRANDO O PROGRAMA.')
            break
        
        else:
            print('Opção Inválida. Por favor escolha uma opção válida.')

if __name__ == "__main__":
    main()