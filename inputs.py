from datetime import datetime


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
        
        if opcao == '1':
            return {'tipo': 'Pix', 'parcelado': False, 'numero_parcelas': None}
        
        elif opcao == '2':
            while True:
                tipo = str(input('À Vista ou Parcelado? (V/P)')).strip().upper()

                if tipo == 'V':
                    return {'tipo': 'Crédito', 'parcelado': False, 'numero_parcelas': None}
                
                elif tipo == 'P':
                    parcelas = input('Número de parcelas: ').strip()
                    if parcelas.isdigit() and int(parcelas) > 0:
                        return {
                            'tipo': 'Crédito',
                            'parcelado': True,
                            'numero_parcelas': int(parcelas)
                        }
                    else:
                        print('Número de parcelas inválido.')
                else:
                    print('Opção inválida. Escolha V ou P')

        elif opcao == '3':
            return {'tipo': 'Débito', 'parcelado': False, 'numero_parcelas': None}
        
        elif opcao == '4':
            return {'tipo': 'Dinheiro', 'parcelado': False, 'numero_parcelas': None}
        
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')