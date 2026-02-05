from datetime import datetime


def escolher_aba():
    while True:
        print('Escolha o tipo de registro:')
        print('1 - Entradas')
        print('2 - Gastos')
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
        if texto and not texto.isnumeric():
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


def pedir_categoria():
    categorias = {
            '1': 'Essencial/Indispensável',
            '2': 'Essencial Variável/Manutenção',
            '3': 'Conforto/Estilo de Vida',
            '4': 'Supérfluo/Desperdício'
        }
    
    while True:
        print('Escolha a categoria: ')
        for k, v in categorias.items():
            print(f"{k} - {v}")
        
        opcao = input('Opção: ').strip()
        if opcao in categorias:
            return categorias[opcao]
        else:
            print("Opção inválida. Por favor, escolha uma categoria válida.")


def pedir_forma_pagamento():
    while True:
        print("Escolha a forma de pagamento:")
        print("1 - Pix")
        print("2 - Crédito")
        print("3 - Débito")
        print("4 - Dinheiro")
        opcao = input("Opção: ").strip()
        formas = {
            '1': 'Pix',
            '2': 'Crédito',
            '3': 'Débito',
            '4': 'Dinheiro'
        }
        if opcao in formas:
            if opcao == '2':
                pergunta = input('À Vista ou Parcelado? (V/P): ').strip().upper()
                if pergunta == 'V':
                    return 'Crédito à Vista'
                elif pergunta == 'P':
                    parcela = input('Número de parcelas: ').strip()
                    if parcela.isdigit() and int(parcela) > 0:
                        return f'Crédito Parcelado em {parcela}x'
                else:
                    print("Opção inválida. Por favor, escolha V para À Vista ou P para Parcelado.")
            return formas[opcao]
        else:
            print("Opção inválida. Por favor, escolha uma forma de pagamento válida.")