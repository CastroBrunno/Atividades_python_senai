from os import sep
from socket import CAN_BCM_RX_ANNOUNCE_RESUME
from tkinter import N
from traceback import print_last


#para printar o nome varias vezes (abaixo)
#Asteristicos (*) significa multiplicador
print("Brasil " *3)

#para printar a primeira, segunda, teiceira ou outras letras da palavra
#lembrete: começar sempre do zero, primeira letra da palavra correspode à zero
#O numero da letra sempre em colchetes []
print("Brasil"[0])


#para imprimir a ultima letra da palavra, ou seja a 6(sexta) letra
print("Brasil"[5])

#Outro modo para imprimir a ultima letra da palavra é colocando entre colchetes -1, siga o exemplo
print("Brasil" [-1])

#para imprimir "rasi" da palavra Brasil, os dois pontos serve para destinar que começa da letra 1 e vai até a letra 4
print("Brasil"[1:5])


#para imprimir o nomero de letras que uma palavra tem, usa-se o codigo "len"
print(len("Brasil"))

#how print if have a letter in the phase, and return true or false
print("a" in "Brasil") 

#como printar uma linha de palavras com um separador entre essas palavras, usando "sep"
print("Brasil", "Argentina", "Japão", "Russia", sep= " // ")

#comando para pular linha, usa-se o comando \n
#tambem pode se usar como separador como no exemplo acima, porém, usando o codigo de pular linha
print("Brasil", "Argentina", "Japão", "Russia", sep= "\n")

'''
para fazer comentarios com mais de uma linha
usa-se as aspas simples para abrir um comentario com mais de uma linha

'''

#para criar uma função usa-se o codigo "def"

#para fazer um triangulo 



print( "    /\   " )
print( "   /  \  " )
print( "  /    \ " )
print( " /______\ ")
print("\n")

#tambem pode ser faszer usando o comando de separador, vista um pouco acima
#desse modo usa-se apenas uma linha

print( "    /\   " ,  "   /  \  " ,  "  /    \ " ,  " /______\ " , sep="\n")
print("\n")



#para fazer uma variaveel, basta escrever o nome da variavel e colocar o sinal de igual, que significa "receber"
nomes=("Bruno" , "Ricardo" , "Leandro" , "Mateus")


#Para fazer uma procura de alguma entidade em uma variavel, basta procurar pela ordem de numero, sendo a primeira entidade respresentada pelo numero 0, a segunda entidade representada pelo numero 1, e assim vai.

print(nomes[2])

#para imprimir duas entidades de alguma variavel sem precisar repetir o comando print, chamamos a variavel novamente e selecionamos o numero da entidade que desejamos

print(nomes[2], nomes[3])

#se quiser podemos usar separadores tambem

print(nomes[1], nomes[3], sep=" & ")


#para conseguir sececionar as letras de uma entidade dentro de uma variavel, segue o exemplo abaixo
#o primeiro numero usado em colchetes é usado para indicar o nome que deseja ser selecionado dentro da variavel nomes, e o segundo colchete é usado para selecionar as letras desejadas de tal palavra
print(nomes[0][1:5])



#input
#modo usado para inserir um dado para uma variavel
#na linha de baixo um dos metodos usado para chamar uma variavel (metodo de contatenação, ou seja metodo de soma, a palavra mais a soma da variavel)
carro= input("Qual é o nome do carro? ")
print("O carro do Bruno é um "+carro)


#metodo para pedir um modelo de carro e depois um modelo de moto
modelmoto= input("Qual o modelo da moto desejada? ")
cormoto= input("Escreva agora a cor desejada? ")

print("O modelo da moto será uma " +modelmoto)
print("A cor da moto será " +cormoto)

#para multiplicar o valor de uma variavel ou de qualquer outro dado, use o nome da variavel ou o nome de qualquer outra coisa e depois insira * (asteristico), e insira o numero de vezes que deseja repetir um dado
#IMPORTANTE: O * (asteristico) é um sinal de multiplicador


#como multiplicar um valor de um dado
moto= input("Informe um modelo de moto: ")
#num_rep= numero de repeticoes que sera usado para a variavel "moto" 
#na variavel 'num_rep' iremos usar o comando "int" para representar que essa variavel só recebera dados do comando inteiro e não "str" string
num_rep= int(input("Informe o numero de vezes que deseja repetir a palavra: "))
print(moto*num_rep)

#como saber o tipo da variavel 
print(type(num_rep))


#como imprimir a quantidade de letras de uma palavra de uma variavel, usa-se o comando "Len"
carroletra= input("Qual o nome do carro que deseja fazer a contagem de letras: ")
quantidade_de_letras= len(carroletra)

print(f"A quantidade de letras é de: {quantidade_de_letras}")

#tentar retornar a primeira letra de uma palavra que entra en uma variavel

nomecarro= input("informe um nome de um carro qualquer: ")
print(f"A primeira letra dessa palavra é {nomecarro[0]}")

#nessa proxima atividade o usuario escolhera dois modelos de carros e o usuario tambem escolhera o estilo de separador que deseja escolher entre os dois modelos dos carros

carroa= input("Informe o nome do carro A: ")
carrob= input("Informe o nome do carro B: ")
separadorcarro= input("Informe o estilo de separador (//, **, ##): ")

print(carroa, carrob, sep= separadorcarro )





























