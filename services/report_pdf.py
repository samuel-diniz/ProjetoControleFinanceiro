from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from database.connection import get_connection
from utils.ui import sucesso


def exportar_pdf(ano):
    doc = SimpleDocTemplate(f'relatorio_{ano}.pdf', pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM gastos
        WHERE strftime('%Y', data) = ?
        GROUP BY categoria
    """, (str(ano),))

    elements.append(Paragraph(f'Relatório Finaceiro {ano}', styles['Title']))
    elements.append(Spacer(1, 20))

    for row in cursor.fetchall():
        elements.append(Paragraph(f'{row[0]}: R$ {row[1]:.2f}', styles['BodyText']))

    conn.close()
    doc.build(elements)

    sucesso("PDF gerado com sucesso.")