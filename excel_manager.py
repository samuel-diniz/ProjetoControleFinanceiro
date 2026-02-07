from openpyxl import load_workbook
from config import arquivo_excel, aba_entradas, aba_gastos

def carregar_planilha():
    try:
        workbook = load_workbook(filename=arquivo_excel)
        return workbook
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar a planilha: {e}")
    

def salvar_entrada(wb, dados):
    ws = wb[aba_entradas]

    ws.append([
        dados['data'].day, 
        dados['data'].month, 
        dados['data'].year,
        dados['descricao'],
        dados['categoria'], 
        dados['valor'],
        dados['forma_de_pagamento']
               ])
  


def salvar_gastos(wb, dados):
    ws = wb[aba_gastos]

    ws.append([
        dados['data'].day, 
        dados['data'].month, 
        dados['data'].year,
        dados['descricao'],
        dados['categoria'], 
        dados['valor_total'],
        dados['forma_de_pagamento'],
        dados['parcelado'],
        dados['numero_parcelas'],
        dados['valor_parcela']
               ])
