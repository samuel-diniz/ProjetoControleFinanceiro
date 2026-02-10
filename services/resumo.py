from collections import defaultdict
from database.connection import get_connection
from database.repository import buscar_resumo_mensal


def gerar_resumo_mensal():
    entradas, gastos = buscar_resumo_mensal()

    resumo = defaultdict(lambda: {'entradas': 0, 'gastos': 0})

    for row in entradas:
        chave = (int(row['mes']), int(row['ano']))
        resumo[chave]['entradas'] = row['total'] or 0

    for row in gastos:
        chave = (int(row['mes']), int(row['ano']))
        resumo[chave]['gastos'] = row['total'] or 0

    print('\n=== RESUMO MENSAL ===')

    for (mes, ano) in sorted(resumo.keys(), key=lambda x: (x[1], x[0])):
        entradas = resumo[(mes, ano)]['entradas']
        gastos = resumo[(mes, ano)]['gastos']
        saldo = entradas - gastos

        print(f'{mes:02d}/{ano} | Entradas: R$ {entradas:.2f} | '
              f'Gastos: R$ {gastos:.2f} | Saldo: R$ {saldo:.2f}')



def obter_saldo_mensal(mes, ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(valor), 0)
        FROM entradas
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))

    total_entradas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            COALESCE(SUM(valor), 0)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))

    total_gastos = cursor.fetchone()[0]

    conn.close()

    return total_entradas - total_gastos