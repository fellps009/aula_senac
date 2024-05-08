'''
#questão 1
numero = int(input("digite um numero"))
divisores = 0
for divisor in range(1, numero):
     if numero % divisor == 0:
        divisores  = divisores + 1
        if divisores > 1:
             break 
if divisores > 1:
    print("não é primo")
else:
    print("é primo")
'''  
'''
#questão 2
def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("Digite uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")
    '''
'''
#questão 3
graus_celsius = float(input("Digite a temperatura em Celsius: "))
graus_farenheit = ((graus_celsius * 9) / 5) + 32
print(f"{graus_celsius:.2f} graus Celsius correspondem a "f"{graus_farenheit:.2f} graus Farenheit")
'''
'''
#questão 4
ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
'''
'''
#questão 5
numeros = [5, 10, 15, 20, 25]
soma = sum(numeros)
media = soma / len(numeros)
print("A média dos números é:", media)
'''
'''
#questão 6
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
elif (a == b) and (a == c) :
        print('Equilatero')
elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
else:
        print('Escaleno')
'''
'''
# questão 7
char=input('Digite um caractere: ')
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
       char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print('Vogal')
else:
     print('Consoante')
     '''


