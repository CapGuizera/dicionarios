#Faça um programa que cadastre n pessoas com nome, idade e altura
nome = []
idade = []
altura = []


people = []
while True:
    if input('Digite e para sair ou 1 para cadastrar: ') == 'e':
        break
    else:
        nome   = (input('Digite o nome: '))
        idade  = (input('Digite a idade: '))
        altura = (input('Digite a altura: '))

        pessoas={'nome' : nome, 'idade' : idade, 'altura' : altura}

        people.append(pessoas)

print(people)