import random 
import os

novo_jogo = 's'

while novo_jogo == 's':
    print(f'Bem vindo ao jogo de adivinhação!')
    print(f'Você terá três chances para advinhar um numero entre 1 e 15.')

    # Gerar o numero aleatorio secreto
    num = random.randint(1,15)

    # Jogar
    for i in range(3):
        print(f'\nQual a sua escolha?')
        chute = int(input())

        if chute == num:
            print(f'\nParabéns, você acertou!')
            break
        elif chute > num:
            print(f'Numero alto')
        else:
            print(f'Numero baixo')

    # Caso não tenha acertado, revelar o número secreto:
    if chute != num:
        print(f'O número secreto era o {num}')

    novo_jogo = input('Deseja jogar outra vez? S para sim, outra tecla para não: ')
    novo_jogo = novo_jogo.lower()

    # Limpar a tela
    os.system('clear')