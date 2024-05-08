
def operacoes_basicas (a, b):
    soma = a + b
    subtracao = a - b 
    multiplicacao = a * b 
    if b != 0:
        divisao = a / b 
    else: 
        print("Divisão não permitida!")

    return soma, subtracao, multiplicacao, divisao

num1 = 10
num2 = 5
resultado = operacoes_basicas(num1, num2) 
print("soma: ", resultado[0])   
print("subtração: ", resultado[1])
print("multiplicação: ", resultado[2])
print("divisão: ", resultado[3])



def fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i 
            return fat 
        
        x = 10 
        print("o fatorial de", x, " e: ", fatorial (x)) 
        

a = input("Digite seu no nome: ")
b = int(input ("digite um número inteiro: "))
c = float(input("digite seu ponto flutuante:"))

soma = c + b

subtracao = c - b 
 
def soma (b , c):
    adicao = b + c
    return soma 
print("soma: ", soma(b,c))


