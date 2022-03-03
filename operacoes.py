import random

class Config:
    def __init__(self):
        self.dif1 = 0
        self.dif2 = 0
        self.QtdExer = 0
        self.RespDif = 0
        self.ValorDificuldade = 0
        self.Score = 0
        self.AcertoQuestao = 0
        self.operacao = 0

def operacao_soma(config):
    AcertoQuestao= config.AcertoQuestao
    Score = 0
    for Cont in range(1, config.QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(config.dif1, config.dif2)
        N2 = random.randint(config.dif1, config.dif2)
        if (config.RespDif == 4):  # Deixar em float
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
            Score = Score + config.ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score

def operacao_subtracao(config):
    AcertoQuestao= config.AcertoQuestao
    Score = 0
    for Cont in range(1, config.QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(config.dif1, config.dif2)
        N2 = random.randint(config.dif1, config.dif2)
        if (config.RespDif == 4):  # Deixar em float
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
            Score = Score + config.ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score


def operacao_divisao(config):
    AcertoQuestao= config.AcertoQuestao
    Score = 0
    for Cont in range(1, config.QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(config.dif1, config.dif2)
        N2 = random.randint(config.dif1, config.dif2)
        if (config.RespDif == 4):  # Deixar em float
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
            Score = Score + config.ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score

def operacao_multi(config):
    AcertoQuestao= config.AcertoQuestao
    Score = 0
    for Cont in range(1, config.QtdExer + 1):
        #Gera os numeros aleatorios
        N1 = random.randint(config.dif1, config.dif2)
        N2 = random.randint(config.dif1, config.dif2)
        # Faz a pergunta para o usuario
        print("{}. {:.2f} X {:.2f} = ?".format(Cont, N1, N2))
        Tentativa = float(input("A resposta é: "))
        Resp = N1 * N2

        # HELP FLAVINHO ! Ta multiplicando errado no modo insano!
        # tirei esse arredondamento ta doido fazer multiplacao com numero quebrado

        # Round pra quando um valor ser tipo 0,897479 ele interpretar que só importa o 0,89
        Resp = round(Resp, 2)
        
        if(Resp == Tentativa):
            print("Voce acertou")
            print("")
            print("")
            # Valor Dificuldade é o valor de cada valor por dificuldade
            Score = Score + config.ValorDificuldade
            AcertoQuestao = AcertoQuestao + 1
        else:
            print("Voce errou!")
            print("")
            print("A resposta certa era: {}".format(Resp))
            print("")
            print("")
        print("=================================")
    return AcertoQuestao, Score