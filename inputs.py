from datetime import datetime
from utils.ui import erro

def pedir_data():
    while True:
        try:
            data = input("Data (DD/MM/AAAA): ").strip()
            return datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            erro("Data inválida. Por favor, insira no formato DD/MM/AAAA.")


def pedir_texto(msg):
    while True:
        texto = str(input(msg)).strip()

        if not texto:
            erro('Campo não pode ser vazio')
            continue
        if texto.isnumeric():
            erro("Por favor, insira um texto válido.")
            continue

        return texto

def pedir_valor(msg):
    while True:
        try:
            valor = float(input(msg).replace(',', '.'))
            if valor <= 0:
                erro('O valor deve ser maior que zero.')
                continue

            return valor
        
        except ValueError:
            erro("Valor inválido. Por favor, insira um número válido.")


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
            erro("Opção inválida. Por favor, escolha uma categoria válida.")


def pedir_forma_pagamento():
    while True:
        print("Escolha a forma de pagamento:")
        print("1 - Pix")
        print("2 - Crédito")
        print("3 - Débito")
        print("4 - Dinheiro")
        
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            return {'tipo': 'Pix', 'parcelado': False, 'numero_parcelas': None}
        
        elif opcao == '2':
            while True:
                tipo = str(input('À Vista ou Parcelado? (V/P)')).strip().upper()

                if tipo == 'V':
                    return {'tipo': 'Crédito', 'parcelado': False, 'numero_parcelas': None}
                
                elif tipo == 'P':
                    parcelas = input('Número de parcelas: ').strip()

                    if not parcelas.isdigit():
                        erro('Digite apenas números')
                        continue
                    
                    parcelas = int(parcelas)

                    if parcelas <= 1:
                        erro('Parcelamento deve ser maior que 1.')
                        continue

                    return {
                        'tipo': 'Crédito',
                        'parcelado': True,
                        'numero_parcelas': int(parcelas)
                    }
                
                else:
                    erro('Opção inválida. Escolha V ou P')

        elif opcao == '3':
            return {'tipo': 'Débito', 'parcelado': False, 'numero_parcelas': None}
        
        elif opcao == '4':
            return {'tipo': 'Dinheiro', 'parcelado': False, 'numero_parcelas': None}
        
        else:
            erro('Opção inválida. Por favor, escolha uma opção válida.')