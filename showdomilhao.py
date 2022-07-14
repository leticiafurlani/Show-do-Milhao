# -*- coding utf-8 -*-

"Show do Milhão "
"Leticia"

print ("show do milhão 1.0")



nome = input("digite seu nome: ")
print("Bem Vindo "+nome)
print('-Escreve as respostas igual está escrito nas alternativas-')

print('1-' "Qual a capital do Brasil?")


lista1 = ['Rio de Janeiro', 'São Paulo', 'Brasília']

for i in lista1:
    print(i)

Resposta = input('Resposta: ')
if Resposta == 'Brasília':
    print('Resposta Correta!')
    x1 = 1
    
if Resposta != 'Brasília':
    print('Resposta Errada')
    x1 = 0

print('2-' "Qual 5ª maravilha do mundo?")

lista2 = ['Cristo Redentor', 'Ruínas de Petra', 'Coliseu']

for i in lista2:
    print(i)
    
Resposta = input('Resposta: ')
if Resposta == 'Ruínas de Petra':
       print('Resposta Correta!')
       x2 = 2
       
if Resposta != 'Ruínas de Petra':
      print('Resposta Errada')       
      x2 = 0

print('3-' "Quem é a mulher do Tarzan?")

lista3 = ['Diana', 'Jane', 'Chita']

for i in lista3:
    print(i)
    
Resposta = input('Resposta: ')
if Resposta == 'Jane':
       print('Resposta Correta!')
       x3 = 1
if Resposta != 'Jane':
      print('Resposta Errada')       
      x3 = 0
      
print('4-' "Qual o coletivo de cães?")

lista4 = ['Alcateia', 'Matilha', 'Rebanho']

for i in lista4:
    print(i)
    
Resposta = input('Resposta: ')
if Resposta == 'Matilha':
       print('Resposta Correta!')
       x4 = 1
if Resposta != 'Matilha':
    print('Resposta Errada')       
    x4 = 0
      
print('5-' "Qual é o antônimo de malograr?")

lista5 = ['Conseguir', 'Fracassar', 'Desprezar']

for i in lista5:
    print(i)
    
Resposta = input('Resposta: ')
if Resposta == 'Conseguir':
       print('Resposta Correta!')
       x5 = 1
if Resposta != 'Conseguir':
    print('Resposta Errada')       
    x5 = 0
      
Resultado = x1 + x2 + x3 + x4 + x5

print('Você fez')
print(Resultado)
print('Pontos')

with open("resultado1.txt", "a") as f:
    f.write (nome +
             str(Resultado) +
             'pontos')
            