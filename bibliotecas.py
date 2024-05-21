'''
import math
numero = 16
raiz_quadrada = math.sqrt(numero)
print("A raiz quadrada de", numero, "é: ",raiz_quadrada)
'''
'''
import random

numero_aleatorio = random.randint(1,100)
print("O número aleatorio é: ", numero_aleatorio)

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print("A lista embaralhada é: ", lista)
'''

import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0

    while True: 
        palpite  = int(input("tente adivinhar o número entre 1 e 100!"))
        #tentativa += 1
        
        if palpite < numero_aleatorio:
            print("número baixo. tente novamente.")
        elif palpite > numero_aleatorio:
            print("número alto. tente novamente")
        else:
            print(f"parabéns!! vocé acertou o número {numero_aleatorio}")
            break

        jogo_adivinhacao()