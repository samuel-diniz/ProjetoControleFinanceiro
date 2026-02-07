from inputs import escolher_aba, pedir_data, pedir_texto, pedir_valor, pedir_categoria, pedir_forma_pagamento
from excel_manager import carregar_planilha, salvar_entrada, salvar_gastos
from datetime import date
from dateutil.relativedelta import relativedelta


def main():
    wb = carregar_planilha()

    aba = escolher_aba()
    if aba is None:
        print("Encerrando o programa.")
        return
    
    elif aba == 'E':
        print("Você escolheu registrar uma nova ENTRADA.")
        data = pedir_data()
        descricao = pedir_texto('Descrição: ')
        categoria = pedir_categoria()
        valor = pedir_valor('Valor: ')
        forma_pagamento = pedir_forma_pagamento()
        salvar_entrada(wb, {
            'data': data,
            'descricao': descricao,
            'categoria': categoria,
            'valor': valor,
            'forma_de_pagamento': forma_pagamento
        })
        print("Entrada registrada com sucesso!")
        
    elif aba == 'G':
        print("Você escolheu registrar um novo GASTO.")
        data = pedir_data()
        descricao = pedir_texto('Descrição: ')
        categoria = pedir_categoria()
        valor = pedir_valor('Valor: ')
        forma_pagamento = pedir_forma_pagamento()

        if forma_pagamento['parcelado']:
            valor_parcela = round(valor / forma_pagamento['numero_parcelas'], 2)

            for i in range(forma_pagamento['numero_parcelas']):
                data_parcela = data + relativedelta(month=i)

                salvar_gastos(wb, {
                'data': data_parcela,
                'descricao': f"{descricao} ({i+1}/{forma_pagamento['numero_parcelas']})",
                'categoria': categoria,
                'valor_total': valor,
                'forma_de_pagamento': forma_pagamento['tipo'],
                'parcelado': True,
                'numero_parcelas': forma_pagamento['numero_parcelas'],
                'valor_parcela': valor_parcela
        })
        else:
            salvar_gastos(wb, {
                'data': data,
                'descricao': descricao,
                'categoria': categoria,
                'valor_total': valor,
                'forma_pagamento': forma_pagamento['tipo'],
                'parcelado': False,
                'numero_parcelas': None,
                'valor_parcela': None
            })
        print('Gasto registrado com sucesso!')

if __name__ == "__main__":
    main()