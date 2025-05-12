import oracledb

def conectar():
    try:
        dsn = oracledb.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = oracledb.connect(user='rm559258', password='170904', dsn=dsn)

        print("Conexão bem-sucedida com o banco de dados!")
        return conn

    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None

import json

def consultar_e_exportar():
    conn = conectar()
    cursor = conn.cursor()

    linha = str(input("Filtrar por qual linha? (8 ou 9): "))
    estacao = input("Filtrar por qual estação (pressione ENTER para ignorar): ")

    if estacao.strip():
        sql = """
            SELECT id, linha, estacao, resposta
            FROM relato_funcionamento
            WHERE linha = :1 AND estacao = :2
        """
        cursor.execute(sql, (linha, estacao))
    else:
        sql = """
            SELECT id, linha, estacao, resposta
            FROM relato_funcionamento
            WHERE linha = :1
        """
        cursor.execute(sql, (linha,))

    resultados = cursor.fetchall()

    if resultados:
        colunas = [desc[0].lower() for desc in cursor.description]
        dados_json = [dict(zip(colunas, linha)) for linha in resultados]

        with open("relatos_exportados.json", "w", encoding="utf-8") as f:
            json.dump(dados_json, f, indent=4, ensure_ascii=False)

        print("Consulta realizada e exportada para 'relatos_exportados.json'.")
    else:
        print("Nenhum resultado encontrado para os filtros aplicados.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    consultar_e_exportar()
