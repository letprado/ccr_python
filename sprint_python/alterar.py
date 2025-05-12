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


def alterar_relato():
    conn = conectar()
    cursor = conn.cursor()

    id_relato = int(input("Digite o ID do relato que deseja alterar: "))
    nova_resposta = input("Digite a nova resposta sobre o funcionamento da estação: ")

    sql = """
        UPDATE relato_funcionamento
        SET resposta = :1
        WHERE id = :2
    """
    cursor.execute(sql, (nova_resposta, id_relato))
    conn.commit()

    if cursor.rowcount > 0:
        print("Relato alterado com sucesso.")
    else:
        print("ID não encontrado.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    alterar_relato()
