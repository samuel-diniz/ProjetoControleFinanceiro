from inputs import escolher_aba, pedir_data, pedir_texto, pedir_valor, pedir_categoria, pedir_forma_pagamento
from excel_manager import carregar_planilha, salvar_entrada, salvar_gastos


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

    

if __name__ == "__main__":
    main()