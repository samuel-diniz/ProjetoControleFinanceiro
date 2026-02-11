from openpyxl import Workbook
from database.connection import get_connection
from utils.ui import sucesso


def exportar_excel(ano):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório"

    ws.append(['Categoria', 'Total'])

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM gastos
        WHERE strftime('%Y', data) = ?
        GROUP BY categoria
    """, (str(ano),))

    for row in cursor.fetchall():
        ws.append([row[0], row[1]])

    conn.close()
    wb.save(f'relatorio_{ano}.xlsx')

    sucesso('Excel gerado com sucesso')