from openpyxl import load_workbook
from config import arquivoExcel, abaEntradas, abaGastos

def carregar_planilha():
    try:
        workbook = load_workbook(filename=arquivoExcel)
        return workbook
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar a planilha: {e}")
    

def salvar_entrada(wb, dados):
    ws = wb[abaEntradas]

    ws.append([dados['data'].day, 
               dados['data'].month, 
               dados['data'].year,
               dados['descricao'],
               dados['categoria'], 
               dados['valor'],
               dados['forma_de_pagamento']
               ])
    wb.save(arquivoExcel)


def salvar_gastos(wb, dados):
    ws = wb[abaGastos]

    ws.append([dados['data'].day, 
               dados['data'].month, 
               dados['data'].year,
               dados['descricao'],
               dados['categoria'], 
               dados['valor_total'],
               dados['forma_de_pagamento'],
               dados['parcelado'],
               dados['numero_de_parcelas'],
               dados['total_parcelas']
               ])
    wb.save(arquivoExcel)