'''
def fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i 
            return fat 
        
        x = int(input("digite um núnero inteiro: "))
        print("o fatorial de", x, " e: ", fatorial (x)) 
'''
'''
idade =  int(input("digite sua idade"))


altura = float(input("digite sua altura:"))


nome = input("digite seu nome:")

tem_carro = input("tem carro? (sim/não): ")

tem_carro + tem_carro.lower() == "sim"

print("idade ", idade)
print("altura ", altura)
print("nome ", nome)
print("tem_carro? ", "sim" if tem_carro else "não")
'''
'''
def contagem_regressiva():
    numero = int(input("digite um número inteiro posirivo:"))

    if numero <= 0:
     print("por favor, digite um número inteiro positivo.")
    contagem_regressiva()

     else:
         while numero >= 0:
                print(numero)
                numero -= 1 

contagem_regressiva()
'''

def soma (a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b 
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "divisao nao permitida"
  
def calculadora(): 
    print("bem_vindo a calculadora em python!")
    print("selecione a opção desejada:")
    print("1: adição")
    print("2: subtração")
    print("3: multiplicação")   
    print("4: divisão")

    escolha = input("Digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))

        if escolha == "1":
            print("resutado", soma(num1, num2))
        elif escolha == "2":
            print("resultado", subtracao(num1, num2))
        elif escolha == "3":
            print("resultado", multiplicacao(num1, num2))
        elif escolha == "4":
            print("resultado", divisao(num1, num2))

    else:
        print("escolha invalida")
    
calculadora()
        