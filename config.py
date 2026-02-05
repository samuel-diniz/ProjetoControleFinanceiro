import pandas as pd 

arquivoExcel = 'controle_financeiro.xlsx'
abaEntradas = 'ENTRADAS'
abaGastos = 'GASTOS'

dfEntradas = pd.read_excel(arquivoExcel, sheet_name=abaEntradas)
dfGastos = pd.read_excel(arquivoExcel, sheet_name=abaGastos)

print(dfEntradas.head())
print(dfGastos.head())