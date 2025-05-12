estacoes = {
    8: {1: "Júlio Prestes", 2: "Palmeiras-Barra Funda", 3: "Lapa", 4: "Domingos de Moraes", 5: "Imperatriz Leopoldina",
        6: "Presidente Altino", 7: "Osasco", 8: "Comandante Sampaio", 9: "Quitaúna", 10: "General Miguel Costa",
        11: "Carapicuíba", 12: "Santa Terezinha", 13: "Antônio João", 14: "Barueri", 15: "Jardim Belval",
        16: "Jardim Silveira", 17: "Jandira", 18: "Sagrado Coração", 19: "Engenheiro Cardoso", 20: "Itapevi",
        21: "Santa Rita", 22: "Amador Bueno"},
    9: {1: "Osasco", 2: "Presidente Altino", 3: "Ceasa", 4: "Villa Lobos-Jaguaré", 5: "Cidade Universitária",
        6: "Pinheiros", 7: "Hebraica-Rebouças", 8: "Cidade Jardim", 9: "Vila Olímpia", 10: "Berrini",
        11: "Morumbi", 12: "Granja Julieta", 13: "Santo Amaro", 14: "Socorro", 15: "Jurubatuba", 16: "Autódromo",
        17: "Primavera-Interlagos", 18: "Grajaú"}
}

def exibir_estacoes(linha):
    if linha in estacoes:
        print(f"Estações da linha {linha}:")
        for num, nome in estacoes[linha].items():
            print(f"{num} - {nome}")
    else:
        print("Linha inválida!")

def calcular_sentido(linha, origem_num, destino_num):
    if linha in estacoes and origem_num in estacoes[linha] and destino_num in estacoes[linha]:
        origem_nome = estacoes[linha][origem_num]
        destino_nome = estacoes[linha][destino_num]
        if destino_num < origem_num:
            sentido = estacoes[linha][origem_num - 1] if origem_num > 1 else "Início da linha"
            print(f"Para ir de {origem_nome} até {destino_nome}, siga no sentido da estação {sentido}.")
        else:
            sentido = estacoes[linha][origem_num + 1] if origem_num < len(estacoes[linha]) else "Fim da linha"
            print(f"Para ir de {origem_nome} até {destino_nome}, siga no sentido da estação {sentido}.")
    else:
        print("Número de estação inválido!")

def salvar_interacao(pergunta, resposta):
    arquivo = open("C:\\temp\\ArquivoPython.txt", "a")
    arquivo.write(f"Pergunta: {pergunta}\nResposta: {resposta}\n")

while True:
    try:
        num = int(input("\nDigite a opção desejada:\n 1 - Quais os nomes das estações? \n 2 - Quais linhas possuem baldeação? \n 3 - Contatos \n 4 - Qual sentido devo ir para chegar ao meu destino? \n 5 - Sair\n"))
        
        salvar_interacao("Digite a opção desejada", str(num))

        if num == 1:
            linha = int(input("\nQual linha você deseja consultar? (8 - Diamante, 9 - Esmeralda): "))
            salvar_interacao("Qual linha você deseja consultar?", str(linha))
            exibir_estacoes(linha)
        
        elif num == 2:
            print("\nBaldeações disponíveis:")
            print("Linha 8 - Diamante: Palmeiras-Barra Funda (linha 3 e 7), Lapa (linha 7), Osasco (linha 9).")
            print("Linha 9 - Esmeralda: Osasco (linha 8), Presidente Altino (linha 8), Pinheiros (linha 4), Berrini (linha 5), Vila Olímpia (linha 4).")
            salvar_interacao("Quais linhas possuem baldeação?", "Informações de baldeações da linha 8 e 9.")
        
        elif num == 3:
            print("\nContatos da ViaMobilidade:\nWhatsApp: (11) 91277-6323 \nTelefone: 0800.770.7106")
            salvar_interacao("Quais são os contatos?", "Contatos ViaMobilidade.")
        
        elif num == 4:
            linha = int(input("\nEscolha a linha (8 - Diamante ou 9 - Esmeralda): "))
            salvar_interacao("Escolha a linha", str(linha))
            exibir_estacoes(linha)
            origem = int(input("Digite o número da estação de origem: "))
            destino = int(input("Digite o número da estação de destino: "))
            salvar_interacao("Digite o número da estação de origem", str(origem))
            salvar_interacao("Digite o número da estação de destino", str(destino))
            calcular_sentido(linha, origem, destino)
        
        elif num == 5:
            print("\nObrigado por utilizar o Vimo! Até mais! :)")
            salvar_interacao("Usuário escolheu sair", "Sair")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
            salvar_interacao("Usuário escolheu uma opção inválida", "Opção inválida.")
    
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        salvar_interacao("Erro", "Entrada inválida.")