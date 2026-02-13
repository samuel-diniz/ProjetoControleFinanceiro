from database.connection import get_connection
import matplotlib.pyplot as plt
from utils.ui import aviso

def grafico_gastos_mensais(mes, ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
        GROUP BY categoria
    """, (f"{mes:02d}", str(ano)))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        aviso('Nenhum gasto encontrado')
        return
    
    categorias = [r[0] for r in rows]
    valores = [r[1] for r in rows]

    plt.figure()
    plt.bar(categorias, valores)
    plt.title(f'Gastos por categoria - {mes:02d}/{ano}')
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def evolucao_saldo(ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            strftime('%m', data) as mes,
            SUM(valor) as total
        FROM entradas
        WHERE strftime('%Y', data) = ?
        GROUP BY mes
    """, (str(ano),))

    entradas = {int(r[0]): r[1] for r in cursor.fetchall()}

    cursor.execute("""
        SELECT 
            strftime('%m', data) as mes,
            SUM(valor) as total
        FROM gastos
        WHERE strftime('%Y', data) = ?
        GROUP BY mes
    """, (str(ano),))

    gastos = {int(r[0]): r[1] for r in cursor.fetchall()}

    conn.close()

    meses = range(1, 13)
    saldos = []

    saldo_acumulado = 0

    for mes in meses:
        e = entradas.get(mes, 0)
        g = gastos.get(mes, 0)
        saldo_acumulado += (e - g)
        saldos.append(saldo_acumulado)

    plt.figure()
    plt.plot(list(meses), saldos)
    plt.title(f'Evolução de Saldo - {ano}')
    plt.xlabel("Mês")
    plt.ylabel("Saldo")
    plt.show()

    