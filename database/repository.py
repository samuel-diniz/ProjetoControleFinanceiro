from database.connection import get_connection

def inserir_entrada(dados):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO entradas (data, descricao, categoria, valor, forma_pagamento)
        VALUES (?, ?, ?, ?, ?)
    """, (
        dados['data'],
        dados['descricao'],
        dados['categoria'],
        dados['valor'],
        dados['forma_pagamento']
    ))

    conn.commit()
    conn.close()


def inserir_gasto(dados):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO gastos (
            data, descricao, categoria, valor,
            forma_pagamento, parcelado, numero_parcelas
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        dados['data'],
        dados['descricao'],
        dados['categoria'],
        dados['valor'],
        dados['forma_pagamento'],
        int(dados['parcelado']),
        dados['numero_parcelas'],
    ))

    conn.commit()
    conn.close()


def buscar_resumo_entradas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            strftime('%m', data) AS mes,
            strftime('Y%', data) AS ano,
            SUM(valor) as total_entradas
        FROM entradas
        GROUP BY ano, mes
    """)

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def buscar_resumo_gastos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            strftime('%m', data) AS mes,
            strftime('%Y', data) AS ano,
            SUM(valor) as total_gastos
        FROM gastos
        GROUP BY ano, mes
    """)

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def buscar_resumo_mensal():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            strftime('%m', data) AS mes,
            strftime('%Y', data) AS ano,
            SUM(valor) AS total
        FROM entradas
        GROUP BY ano, mes
    """)
    entradas = cursor.fetchall()

    cursor.execute("""
        SELECT 
            strftime('%m', data) AS mes,
            strftime('%Y', data) AS ano,
            SUM(valor) AS total
        FROM gastos
        GROUP BY ano, mes
    """)
    gastos = cursor.fetchall()

    conn.close()
    return entradas, gastos