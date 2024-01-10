#Média Ponderada dos alunos // Students' Weighted Average

print ("-"*30)
print ("Use esse sistema para calcular as médias ponderadas de acordo com os pesos desejados")
print ("-"*30)



#Função para obter os pesos das notas
def obter_pesos(nota):
    #while para criar um loop até o usuário digitar os valores válidos
    while True:
        #try-except para validar os valores
        try:
            peso = float(input(f"Digite o valor do {nota} peso: "))

            if 0 <= peso <= 10:
                break
            else:
                print("Valor inválido, por favor digite um valor válido entre 0.0 e 10.0")

        except ValueError:
            print("Valor inválido, por favor digite um número entre 0.0 e 10.0")

    return peso

#Função para obter os numeros de estudantes
def obter_numeros_estudantes():
    while True:
        try:
            numEstudantes = int(input("Digite o número de estudantes: "))

            if numEstudantes > 0:
                break
            else:
                print("Número inválido, por favor digite um número acima de 0")

        except ValueError:
            print("Valor inválido, por favor digite um número inteiro")

    return numEstudantes


#Função para obter os nomes dos estudantes de acordo com a quantidade desejada
def obter_nomes_estudantes(num_estudantes):
    nomes_estudantes = []
    for i in range(num_estudantes):
        nome = input(f"Digite o nome do estudante {i + 1}: ")
        nomes_estudantes.append(nome)

    return  nomes_estudantes

#Nessa função pedimos as notas de acordo com cada estudante
def obter_notas(nomes_estudantes):
    notas_estudantes = {} #Aqui criamos um dicionário onde armazena as notas de acordo com as chaves que são os nomes
    for nome in nomes_estudantes:
        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1} de {nome}: "))
                    if 0<= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida, por favor digite um número entre 0 e 10")
                except ValueError:
                        print("Valor inválido, por favor digite um número")

        notas_estudantes[nome] = notas
    return notas_estudantes

#
def calcular_media(notas_estudantes):
    medias_estudantes = {}

    for nome, notas in notas_estudantes.items():
        media_ponderada = (notas[0] * peso1 + notas[1] * peso2 + notas[2] * peso3) / (peso1 + peso2 + peso3)
        medias_estudantes[nome] = media_ponderada

    return medias_estudantes

def imprimir(notas_estudantes, medias_estudantes):
    print("\nNotas e médias dos estudantes: ")
    for nome, notas in notas_estudantes.items():
        media = medias_estudantes[nome]
        print(f"{nome}: {notas}, Média Ponderada: {media: .1f}")

#No final do código chamamos todas as funções
peso1 = obter_pesos("primeiro")
peso2 = obter_pesos("segundo")
peso3 = obter_pesos("terceiro")
numeroEstudantes = obter_numeros_estudantes()
nomeEstudantes = obter_nomes_estudantes(numeroEstudantes)
notas_estudantes = obter_notas(nomeEstudantes)
medias_estudantes = calcular_media(notas_estudantes)
imprimir(notas_estudantes, medias_estudantes)


