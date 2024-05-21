'''
def soma_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return sum(impares)

numeros = input("digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]
soma = soma_impares(numeros)
print("A soma dos números impares da lista é: ", soma)
'''
'''
def mair_elemento(lista):
    return
mumeros = input("digite os números de lista separados por espaço: ").split()
numeros = [int(num) for num in mumeros] 

maior = mair_elemento(numeros)
print("o maior elemento da lista é: ", maior)
'''

num_alunos = int(input("Quantos alunos deseja registrar?"))

media_alunos = []
media_turma = []

for i in range(1, num_alunos+1):
    print(f"Aluno{1}: ")
    nota_alunos = []

    for j in range(1, 4):
        nota = float(input(f"insira a nota {j}: "))
        nota_alunos.append(nota)
        media_turma.append(nota)

        media_alunos = sum(nota_alunos) / len(nota_alunos)
        media_alunos.append(media_alunos)
        print("a media do aluno é: ", media_alunos)
