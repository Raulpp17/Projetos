####### PROTÓTIPO JOGO ZOMBIE DICE #######

import random

print('Bem vindo ao Zombie Dice\n')

def Jogador(N_Jogadores):
    #N_jogadores = 0
    while (N_jogadores < 2):
        N_jogadores = int(input('Qual o numero de jogadores? '))
        if N_jogadores < 2:
            print('Aviso: Voce precisa de 2 jogadores no minimo\n')
    L_jogadores = []
    for i in range(N_jogadores):
        nome = input('Qual o nome do jogador' + str(i+1) + ': ')
        L_jogadores.append(nome)
    return(L_jogadores)


def Dados(listaDados):
    D_verde = 'CPCTPC'
    D_amarelo = 'TPCTPC'
    D_vermelho = 'TPTCPT'

    listaDados = [
    		D_verde, D_verde, D_verde,D_verde ,D_verde ,D_verde,
    		D_amarelo, D_amarelo, D_amarelo, D_amarelo,
    		D_vermelho,D_vermelho,D_vermelho
        ]
    #return (listaDados)

  #  for i in range(0,3):
 #       Numero_sorteado = random.randrange(0, 12)
#        dado = listaDados[Numero_sorteado]
        #if dado == 'CPCTPC':
         #   corDado = 'VERDE'
        #elif dado == 'TPCTPC': eh du caraio
       #     corDado = 'AMARELO'
      #  else:
     #       corDado = 'VERMELHO'
    #    print('Dado sorteado', i+1, ': ', corDado)
   #     D_Sorteados.append(dado)
  #  return()

print('---INICIANDO O JOGO---')
J_atual = 0
D_Sorteados = []
tiros = 0
cerebros = 0
passos = 0

while(True):

    print('Turno do jogador ', Jogador[J_atual])
    input('---Aperte Enter para sortear os dados---')

    for i in range(0,3):
        Numero_sorteado = random.randrange(0, 12)
        dado = Dados(listaDados=[Numero_sorteado])
        if dado == 'CPCTPC':
            corDado = 'VERDE'
        elif dado == 'TPCTPC':
            corDado = 'AMARELO'
        else:
            corDado = 'VERMELHO'
        print('Dado sorteado', i+1, ': ', corDado)
        D_Sorteados.append(dado)
    input('---Aperte Enter para jogar os dados---')

    print('As faces sorteadas foram: ')
    for dado in D_Sorteados:
        numFaceDado = random.randrange(0, 5)
        if dado[numFaceDado] == "C":
            print('- CÉREBRO (você comeu um cérebro)')
            cerebros+=1
        elif dado[numFaceDado] == "T":
            print('- TIRO (você levou um tiro)')
            tiros+=1
        else:
            print('- PASSOS (uma vítima escapou)')
            passos+=1
    print('\n')
    print('SCORE ATUAL: ')
    print('CÉREBROS: ', cerebros)
    print('TIROS: ', tiros)

    Turno=(input('AVISO: Você deseja continuar jogando dados? (s/n): '))

    if Turno == 'n':
        J_atual = J_atual + 1
        D_Sorteados = []
        tiros = 0
        cerebros = 0
        passos = 0

        if J_atual == len(Jogador()):#--> L
            print('---Finalizando protótipo do jogo---')
            break

    else:
        print('Iniciando mais uma rodada do turno atual')
        D_Sorteados = []

