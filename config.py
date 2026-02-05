import pandas as pd 

arquivo_excel = 'controle_financeiro.xlsx'
aba_entradas = 'ENTRADAS'
aba_gastos = 'GASTOS'

df_entradas = pd.read_excel(arquivo_excel, sheet_name=aba_entradas)
df_gastos = pd.read_excel(arquivo_excel, sheet_name=aba_gastos)

print(df_entradas.head())
print(df_gastos.head())