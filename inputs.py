from datetime import datetime


def escolher_aba():
    while True:
        print('Escolha o tipo de registro:')
        print('1 - Entrada')
        print('2 - Gasto')
        print('0 - Sair')
        opcao = input('Opção: ').strip()
        if opcao == '1':
            return 'E'
        elif opcao == '2':
            return 'G'
        elif opcao == '0':
            return None
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def pedir_data():
    while True:
        try:
            data = input("Data (DD/MM/AAAA): ").strip()
            return datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Por favor, insira no formato DD/MM/AAAA.")


def pedir_texto(msg):
    while True:
        texto = str(input(msg)).strip()
        if texto and texto.isnumeric():
            return texto
        else:
            print("Entrada inválida. Por favor, insira um texto válido.")


def pedir_valor(msg):
    while True:
        try:
            valor = float(input(msg).replace(',', '.'))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")