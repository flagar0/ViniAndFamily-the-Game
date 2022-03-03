import random
from operacoes import *
# Biblioteca que vai saber caso o arquivo já exista
from os.path import exists as file_exists


# desenvolver, um modo prova(mais ponto, mas tem tempo), outros tipos de conta( * / - bhaskara)
# Fazer design
# Desenvolver uma loja


def Bemvindo():
    print("===============================")
    print("\tGerador de contas(Soma)")
    # \t é tabulação, ou seja um tab
    print("===============================")
    print("Desenvolvido por @ViniLinharesBozzon")
    print("Participação de  @Flagar0")
# ==========================


def Arquivo():
    if file_exists('Score.txt'):
        AbrindoR = open("Score.txt", 'r')
        for valor in AbrindoR:
            valor = float(valor)
        AbrindoR.close()
        ScoreG = float(Score + valor)
        ValorArmazenado = str(ScoreG)
        EscrevendoW = open("Score.txt", 'w')
        EscrevendoW.write(ValorArmazenado)
        EscrevendoW.close()
    else:
        CriandoArq = open("Score.txt", 'w+')
        ValorArmazenado = str(Score)
        CriandoArq.write(ValorArmazenado)
        ScoreG = Score
    return ScoreG
# ==========================


def dificuldade():
    print("\n\nQual a operação que voce deseja práticar ?")
    print("[1] Soma")
    print("[2] Subtracao")
    print("[3] Multiplacao")
    print("[4] Divisao")
    print("[5] Voltar ao menu")
    RespDif = int(input(""))
    if (RespDif == 1):
        operacao = "soma"
        diff = 1
    elif (RespDif == 2):
        operacao = "sub"
        diff = 2
    elif (RespDif == 3):
        operacao = "multi"
        diff = 3
    elif (RespDif == 4):
        operacao = "div"
        diff = 3.5

    print("\n\nQual a dificuldade que voce deseja práticar ?")
    print("[1] Fácil")
    print("[2] Médio")
    print("[3] Difícil")
    print("[4] Insano")
    print("[5] Voltar ao menu")
    RespDif = int(input(""))
    if (RespDif == 1):
        dificuldade1 = int(0)
        dificuldade2 = float(5)
        ValorDificuldade = 1*diff
    elif (RespDif == 2):
        dificuldade1 = int(0)
        dificuldade2 = int(10)
        ValorDificuldade = 1.5*diff
    elif (RespDif == 3):
        dificuldade1 = int(3)
        dificuldade2 = int(50)
        ValorDificuldade = 2*diff
    elif (RespDif == 4):
        dificuldade1 = int(234)
        dificuldade2 = int(10000)
        ValorDificuldade = 5*diff
    else:
        dificuldade1 = int(0)
        dificuldade2 = int(5)
    # Voltar ao menu

    # Salva dados na  config
    configs.dif1 = dificuldade1
    configs.dif2 = dificuldade2
    configs.ValorDificuldade = ValorDificuldade
    configs.RespDif = RespDif
    configs.operacao = operacao
# ==========================


def Ortografia(Score):
    if (Score > 1) or (Score == 0):
        print("Voce fez {} pontos.".format(Score))
    else:
        print("Voce fez {} ponto.\n".format(Score))


#                           INICIO

Bemvindo()
Continuacao = "S"
RespDif = 0
AcertoQuestao = 0
configs = Config()

while (Continuacao == "S"):
    Score = 0
    # Cria OBJ com as configs
    dificuldade()

    # QtdExer - Serão as quantidades escolhidas pelo usuário de exercício
    QtdExer = int(input("\nQuantos exercícios voce deseja realizar ? "))
    Cont = 0
    Resp = float(0)

    # Add nas configs
    configs.QtdExer = QtdExer

    # Faz operacao soma
    if(configs.operacao == "soma"):
        AcertoQuestao, Score = operacao_soma(configs)

    # Faz operacao subtracao
    if(configs.operacao == "sub"):
        AcertoQuestao, Score = operacao_subtracao(configs)

    if(configs.operacao == "multi"):
        AcertoQuestao, Score = operacao_multi(configs)

    if(configs.operacao == "div"):
        AcertoQuestao, Score = operacao_divisao(configs)

    if(AcertoQuestao > 1) or (AcertoQuestao == 0):
        print("Voce acertou {} exercícios.".format(AcertoQuestao))
    else:
        print("Voce acertou {} exercício".format(AcertoQuestao))
    Ortografia(Score)
    ScoreG = Arquivo()
    Continuacao = str(input("Voce deseja praticar denovo? {S/N}\n"))
    if (Continuacao == 's'):
        Continuacao = Continuacao.upper()
# Função abrindo arquivo
print("\nSua pontuação total é de: {} ".format(ScoreG))
