from inputs import pedir_data, pedir_texto, pedir_valor, pedir_categoria, pedir_forma_pagamento
from excel_manager import salvar_entrada, salvar_gastos
from dateutil.relativedelta import relativedelta
from config import arquivo_excel


def registrar_entrada(wb):
    print("Você escolheu registrar uma nova ENTRADA.")
        
    dados = {
        'data': pedir_data(),
        'descricao': pedir_texto('Descrição: '),
        'categoria': pedir_categoria(),
        'valor': pedir_valor('Valor: '),
        'forma_de_pagamento': pedir_forma_pagamento()['tipo']
    }   
    salvar_entrada(wb, dados)
    wb.save(arquivo_excel)
        

def registrar_gasto(wb):
    print("Você escolheu registrar um novo GASTO.")
    data = pedir_data()
    descricao = pedir_texto('Descrição: ')
    categoria = pedir_categoria()
    valor = pedir_valor('Valor: ')
    forma_pagamento = pedir_forma_pagamento()

    if forma_pagamento['parcelado']:
        num_parcelas = forma_pagamento['numero_parcelas']
        valor_parcela = round(valor / num_parcelas, 2)

        for i in range(num_parcelas):

            salvar_gastos(wb, {
                'data': data + relativedelta(months=i),
                'descricao': f"{descricao} ({i+1}/{num_parcelas})",
                'categoria': categoria,
                'valor_total': valor,
                'forma_de_pagamento': forma_pagamento['tipo'],
                'parcelado': True,
                'numero_parcelas': num_parcelas,
                'valor_parcela': valor_parcela
        })

            
    else:
        salvar_gastos(wb, {
            'data': data,
            'descricao': descricao,
            'categoria': categoria,
            'valor_total': valor,
            'forma_de_pagamento': forma_pagamento['tipo'],
            'parcelado': False,
            'numero_parcelas': None,
            'valor_parcela': None
        })
    wb.save(arquivo_excel)
    