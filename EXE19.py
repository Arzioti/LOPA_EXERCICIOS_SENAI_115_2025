#    19. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
#      - A média aritmética das duas notas de cada aluno; e
#      - A mensagem que está na tabela a seguir:
#
#           - Média Aritmética      -    Mensagem
#
#              - Até 3             |   Reprovado
#              - Entre 3 e 7       |   Exame
#             - De 7 para cima    |   Aprovado
#
#     O total de alunos aprovados;
#     O total de alunos de exame;
#     O total de alunos reprovados;
#     A média da classe.

#=======================================================================

contAlunos = 1  # inicializa a contagem de alunos
qtdAlunos = 3   # inserir nessa var a quantidade de alunos
qtdnotas = 2    # inserir a quantidade de notas
Somamedias = 0
#######################################
# Variaveis de controle

qtdAprovados = 0
qtdReprovados = 0
qtdExame = 0
########################################

#while True:
while contAlunos <= qtdAlunos:
    print('\n')
    print('#########################')
    print('\n')
    print(f'Aluno {contAlunos}') # Aluno 1 contador na proxima linha;

    nota1 = int(input(f'Insira a primeira nota do Aluno {contAlunos}: '))
    nota2 = int(input(f'Insira a segunda nota do Aluno {contAlunos}: '))

    media = (nota1 + nota2)/qtdnotas
    Somamedias += media


    if media < 3:
        print('Reprovado')
        qtdReprovados += 1 
    elif media >= 3 and media < 7:
        print('Exame')
        qtdExame += 1
    elif media > 7:
        print('Aprovado')
        qtdAprovados += 1

    contAlunos += 1 # contAlunos = contAlunos + 1 incrementando alunos

mediaClasse = Somamedias/qtdAlunos

print('#########################')
print('Reumo Classe: ')
print('\n')
print(f'Alunos Aprovados: {qtdAprovados}.')
print(f'Alunos Reprovados: {qtdReprovados}.')
print(f'Alunos Exame: {qtdExame}.')
print('\n')
print(f'Media Classe: {mediaClasse}.')
print('\n')






   
    