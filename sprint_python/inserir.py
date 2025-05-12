import oracledb

def inserir_registro():
    try:
        dsn = oracledb.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
        conn = oracledb.connect(user='rm559258', password='170904', dsn=dsn)

        cursor = conn.cursor()
        
        linha = int(input("Digite a linha (ex: 8 para Diamante, 9 para Esmeralda): "))
        estacao = input("Digite o nome da estação: ")
        resposta = input("As funcionalidades (escada, elevador) que utilizou hoje estão funcionando? Descreva: ")

        id_gerado = cursor.var(int)  

        cursor.execute("""
            INSERT INTO relato_funcionamento (linha, estacao, resposta)
            VALUES (:linha, :estacao, :resposta)
            RETURNING id INTO :id
        """, linha=linha, estacao=estacao, resposta=resposta, id=id_gerado)

        conn.commit()
        print(f"\nRegistro inserido com sucesso! Seu ID é: {id_gerado.getvalue()}")
    
    except oracledb.DatabaseError as e:
        print(f"Erro ao inserir o registro: {e}")
    
    finally:
        cursor.close()
        conn.close()

def main():
    inserir_registro()

if __name__ == "__main__":
    main()

