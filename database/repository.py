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


def obter_totais_mes(mes, ano):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM entradas
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    entradas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM gastos
        WHERE strftime('%m', data) = ?
        AND strftime('%Y', data) = ?
    """, (f"{mes:02d}", str(ano)))
    gastos = cursor.fetchone()[0]

    conn.close()
    return entradas, gastos


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


def atualizar_entrada(id, novos_dados):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE entradas
        SET data = ?, descricao = ?, categoria = ?, valor = ?, forma_pagamento = ?
        WHERE id = ?
    """, (
        novos_dados['data'],
        novos_dados['descricao'],
        novos_dados['categoria'],
        novos_dados['valor'],
        novos_dados['forma_pagamento'],
        id
    ))

    conn.commit()
    conn.close()

def atualizar_gasto(id, novos_dados):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE gastos
        SET data = ?, descricao = ?, categoria = ?, valor = ?, forma_pagamento = ?
        WHERE id = ?
    """, (
        novos_dados['data'],
        novos_dados['descricao'],
        novos_dados['categoria'],
        novos_dados['valor'],
        novos_dados['forma_pagamento'],
        id
    ))

    conn.commit()
    conn.close()


def listar_entradas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, data, descricao, categoria, valor, forma_pagamento
        FROM entradas
        ORDER BY data DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def listar_gastos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, data, descricao, categoria, valor, forma_pagamento
        FROM gastos
        ORDER BY data DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows