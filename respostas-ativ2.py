# questão 6
'''
def fatorial(n):
    resultado = 1 
    for i in range(2, n+1):
        resultado *= i


numero = int (input("Digite um número inteiro: "))
print(f"Fatorial de {numero} é de {fatorial(numero)}")
'''

# questão 7
     '''
import re

def validar_senha(senha):
    if (len(senha) >= 8 and
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and
        re.search(r"\d", senha) and
        re.search(r"[!@#$%¨&*?/:;.<>,^~`=ç<>\|\()[]{}]")):
        return True 
    else:
        return False
    '''

#Questão 5 

def lista_de_compras():
     compras = [] 

     while True:
          print("Menu da lista de compras !")
          print("1. Adicionar item")
          print("2. remover item")
          print("3. visualizar item")
          print("4. sair")
          escolha = input("Digite o número da opção desejada")

          if escolha == "1":
               item = input("Digite o item que deva ser adicionar")
               compras.append(item)
          elif escolha == "2":
               item = input("Digite o utem que quer remover")
               if item in compras:
                    compras.remover(item)
               else:
                    print("Está tentando remover algo que nunca existiu!")
          elif escolha == "3":
               print("Item da lista de compras até agora: ")
               for item  in compras:
                    print(item)
          elif escolha == "4":
               print("saindo...")
               break
          else:
               print("Opção invalida. tente novamente!")
                

   
   
    