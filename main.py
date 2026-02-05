from inputs import escolher_aba, pedir_data, pedir_texto, pedir_valor


aba = escolher_aba()
if aba is None:
    print("Encerrando o programa.")
    exit()
elif aba == 'ENTRADAS':
    print("Você escolheu registrar uma nova ENTRADA.")
else:
    print("Você escolheu registrar um novo GASTO.")

data = pedir_data()
descricao = pedir_texto("Descrição:")
valor = pedir_valor("Valor:")

print(f'Data: {data}')
print(f'Descrição: {descricao}')
print(f'Valor: R$ {valor:.2f}')