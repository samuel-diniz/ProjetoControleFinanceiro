from inputs import pedir_data, pedir_texto, pedir_valor, pedir_categoria, pedir_forma_pagamento
from database.repository import inserir_entrada, inserir_gasto
from dateutil.relativedelta import relativedelta
from utils.ui import sucesso


def registrar_entrada():
    print("Você escolheu registrar uma nova ENTRADA.")
        
    dados = {
        'data': pedir_data(),
        'descricao': pedir_texto('Descrição: '),
        'categoria': pedir_categoria(),
        'valor': pedir_valor('Valor: '),
        'forma_pagamento': pedir_forma_pagamento()['tipo']
    }   
    inserir_entrada(dados)
    sucesso('ENTRADA REGISTRADA COM SUCESSO!')
        

def registrar_gasto():
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

            inserir_gasto({
                'data': data + relativedelta(months=i),
                'descricao': f"{descricao} ({i+1}/{num_parcelas})",
                'categoria': categoria,
                'valor': valor_parcela,
                'forma_pagamento': forma_pagamento['tipo'],
                'parcelado': True,
                'numero_parcelas': num_parcelas
        })

            
    else:
        inserir_gasto({
            'data': data,
            'descricao': descricao,
            'categoria': categoria,
            'valor': valor,
            'forma_pagamento': forma_pagamento['tipo'],
            'parcelado': False,
            'numero_parcelas': None
        })
    sucesso('GASTO REGISTRADO COM SUCESSO!')
    