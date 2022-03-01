import random

def operacao_soma(dif1, dif2, RespDif, QtdExer, ValorDificuldade, Score,AcertoQuestao):
    for Cont in range(1, QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(dif1, dif2)
        N2 = random.randint(dif1, dif2)
        if (RespDif == 4):  # Deixar em float
            N3 = round(random.random(), 2)
            N3 = (N3/0.09)
            N4 = round(random.random(), 2)
            N4 = (N4/0.09)
            N1 = N1 + N3
            N2 = N2 + N4
        
        # Faz a pergunta para o usuario
        print("{}. {:.2f} + {:.2f} = ?".format(Cont, N1, N2))
        Tentativa = float(input("A resposta é: "))
        Resp = N1 + N2

        # Round pra quando um valor ser tipo 0,897479 ele interpretar que só importa o 0,89
        Resp = round(Resp, 2)
        if(Resp == Tentativa):
            print("Voce acertou")
            print("")
            print("")
            # Valor Dificuldade é o valor de cada valor por dificuldade
            Score = Score + ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score

def operacao_subtracao(dif1, dif2, RespDif, QtdExer, ValorDificuldade, Score,AcertoQuestao):
    for Cont in range(1, QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(dif1, dif2)
        N2 = random.randint(dif1, dif2)
        if (RespDif == 4):  # Deixar em float
            N3 = round(random.random(), 2)
            N3 = (N3/0.09)
            N4 = round(random.random(), 2)
            N4 = (N4/0.09)
            N1 = N1 + N3
            N2 = N2 + N4
        
        # Faz a pergunta para o usuario
        print("{}. {:.2f} - {:.2f} = ?".format(Cont, N1, N2))
        Tentativa = float(input("A resposta é: "))
        Resp = N1 - N2

        # Round pra quando um valor ser tipo 0,897479 ele interpretar que só importa o 0,89
        Resp = round(Resp, 2)
        if(Resp == Tentativa):
            print("Voce acertou")
            print("")
            print("")
            # Valor Dificuldade é o valor de cada valor por dificuldade
            Score = Score + ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score


def operacao_divisao(dif1, dif2, RespDif, QtdExer, ValorDificuldade, Score,AcertoQuestao):
    for Cont in range(1, QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(dif1, dif2)
        N2 = random.randint(dif1, dif2)
        if (RespDif == 4):  # Deixar em float
            N3 = round(random.random(), 2)
            N3 = (N3/0.09)
            N4 = round(random.random(), 2)
            N4 = (N4/0.09)
            N1 = N1 + N3
            N2 = N2 + N4
        
        # Faz a pergunta para o usuario
        print("{}. {:.2f} / {:.2f} = ?".format(Cont, N1, N2))
        Tentativa = float(input("A resposta é: "))
        Resp = N1 / N2

        # Round pra quando um valor ser tipo 0,897479 ele interpretar que só importa o 0,89
        Resp = round(Resp, 2)
        if(Resp == Tentativa):
            print("Voce acertou")
            print("")
            print("")
            # Valor Dificuldade é o valor de cada valor por dificuldade
            Score = Score + ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score