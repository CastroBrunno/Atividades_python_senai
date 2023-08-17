#Faça um programa que leia a idade de 6 empregados, ou seja, tem que inserir 6 idades.

#o comando "while" significa "enquanto", ou seja, enquanto uma condição não se realizar, ele continuara se repetindo, ou seja, while serve como um repetidor.
'''
contador=0
while(contador < 6):
    idade=int(input("Informe a idade do empregado: "))
    contador = contador + 1
#o contador= contador +1 serve para que sempre que o codigo acima dele rodar, ele saber que ja foi rodado uma vez, por exemplo: contador= contador + 1. resultado 1 (ja que na variavel declaramos que o contador é igual a 0), contador= contador + 1. resultado 2, e assim vai
'''


#para fazer a soma das idades inseridas usaremos a mesma estrutura com algumas modificações, segue o exeplo abaixo:
total=0
contador=0
while(contador < 6):
    idade=int(input("Informe a idade do empregado: "))
    total= total + idade
    contador = contador + 1
print("A soma das idades é igual á ", +total)
