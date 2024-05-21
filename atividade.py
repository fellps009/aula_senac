numeros = input ("digite um número separado: ").split()
numeros = [int(numero) for numero in numeros]
y = 0
for numero in numeros:
    if numero % 2 != 0:
        y = y+1
print(y)
