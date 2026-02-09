from datetime import date
from excel_manager import carregar_planilha
from services.finance import registrar_entrada, registrar_gasto
from services.resumo import gerar_resumo_mensal


def menu_principal():
    print('\n=== CONTROLE FINANCEIRO ===')
    print('1 - Registrar entrada')
    print('2 - Registrar gasto')
    print('3 - Atualizar resumo mensal')
    print('4 - Ver saldo do mês atual')
    print('0 - Sair')
    return input('Escolha uma opção: ').strip()


def ver_saldo_atual(wb):
    hoje = date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    ws_resumo = wb['RESUMO']

    for row in ws_resumo.iter_rows(min_row = 2, values_only=True):
        mes, ano, entradas, gastos, saldo = row

        if mes == mes_atual and ano == ano_atual:
            print(f'\nSALDO de {mes:02d}/{ano}: R$ {saldo:.2f}')
            return
    print(f'Nenhum registro encontrado para {mes_atual:02d}/{ano_atual}')


def main():
    wb = carregar_planilha()
    
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            registrar_entrada(wb)
        
        elif opcao == '2':
            registrar_gasto(wb)
        
        elif opcao == '3':
            gerar_resumo_mensal()
            print('RESUMO MENSAL ATUALIZADO!')
        
        elif opcao == '4':
            ver_saldo_atual(wb)
        
        elif opcao == '0':
            print('ENCERRANDO O PROGRAMA.')
            break
        
        else:
            print('Opção Inválida. Por favor escolha uma opção válida.')

if __name__ == "__main__":
    main()