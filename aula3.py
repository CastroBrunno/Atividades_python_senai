#para imprimir um print com mais de uma linha, você pode usar 3 vezes as aspas duplas ("")
print("""Essa seria a maneira de fazer um print com mais de uma linha
voce pode escrever em quantas linhas quiser
só nao se esqueça de fechar com 3 aspas duplas""")

#Imprima o nome de dois carros escolhidos pelo usuario em linhas diferentes
##carroa=input("Insira o nome do carro A: ")
##carrob=input("Insira o nome do carro B: ")
##print(carroa, carrob, sep="\n")

#imprima o valor de tres carros escolhidos pelo o usuario
caroa=input("Informe o nome do carro A: ")
carob=input("Informe o nome do carro B: ")
caroc=input("Informe o nome do carro C: ")
lista= caroa, carob, caroc

posicao=int(input("Informe qual nome de carro deseja imprimir, se é 1º, 2º ou 3º: "))
#no python sabemos que para imprimir o primeiro dado de uma variavel, deve se imprimir o numero 0, pois na sequencia da linguagem o numero 0 corresponde ao primeiro dado, o numero 1 corresponde ao segundo dado, e assim vai
#porem umas das maneira de mudar isso seria chamando a lista onde estao inseridos esses dados e subtraindo menos um numero, assim quando a pessoa chamar o dado numero 1, ele ira subtrair e na verdade chamar o dado numero zero, sendo assim, a partir desse momento o dado numero 1 correspondera ao primeiro dado, sendo assim, se o usuario escolher o numero 1, aparecerá o carroA
print(lista[posicao -1])

letra=int(input("Informe a posição da letra que deseja imprimir, 1º, 2º, 3º ou 4º...: "))
print(lista[posicao -1][letra -1])
#acima foi usado o metodo de subtração para chegar na posição do carro correto e tambem na posição da letra correta, sendo assim, quando o usuario solicitar imprimir a primeira letra, ele enviara o numero 1, e o comando fazera a subtração, ou seja 1-1=0 entra ele imprimira a letra 0
#EXPLICAÇÂO DO PRINT: o primeiro variavel do print é a lista que foi criada pelo usuario, a variavel posição é a escolha que o usuario fez de qual carro ele queria, se era o primeiro, segundo ou terceiro carro, e por ultimo a variavel letra, que retornara qual letra o usuario quer imprimir do carro que ele deseja, ou seja a primeira letra, a segunda e assim vai, e usando o mesmo metodo de subtração usado na variavel "posicao".


num1= int (input("Informe o primeiro numero: "))
num2= int (input("Informe o segundo numero: "))
soma= num1+num2
mult= num1*num2
div= num1/num2
print(f"A soma de {num1} e {num2} é de {soma}")
print(f"A multiplicação de {num1} e {num2} é de {mult}")
print(f"A divisão de {num1} e {num2} é de {div}")

#modo de colocar quantas casas decimais deseja ultilizar no codigo: %.2f"%
#o numero dois no comando serve para dizer quantas casas decimais vc deseja ter depois da virgula, ja as aspas sao ultilizadas para fechar o texto que foi aberto no comando print
#exemplo: print("o resultado é %.2f"% + divisao) ou usar apenas: print("%.2f"% +divisão)


#int: Inteiro, Str: string e float: que mostra casas decimais


#para saber o resto de uma divisão usamos %, segue o exemplo
print(num1%num2)

#duas barras (//) significa cociente, ou seja quantas vezes o numero precisou ser multiplcado para chegar ao resultado

#CONDICIONAIS: 
'''

numero= int(input("Usuário, informe um número: "))
if numero > 0:
    print("Numero positivo")
else:
    if numero < 0:
         print("Numero negativo")
    else:
        if(numero ==0): #Se quisermos retirar esse comando "if", poderiamos, pois iria ter o valor do mesmo jeito, porque se ele nao for maior nem menor, ele so pode ser igual a 0
            print("valor nulo")
            '''
        
#sinal de diferente: A != B  ( A é diferente de B)        

#um modo de encurtar esse codigo seria desta maneira
# O elif seria uma junção de Else + if.
'''
numero= int(input("Usuário, informe um número: "))
if numero > 0:
    print("Numero positivo")
elif numero < 0:
         print("Numero negativo")
else:
         print("valor nulo")
         '''

#para transformar uma frase toda em maiuscula é usado o .upper
#para transformar uma frase toda em minuscula é usado o .lower
#e para transformar a primeira letra de cada palavra em maiuscula é usado o .title
#exemplo: print(nome.upper), (nome.lower) ou (nome.title)

frase= str(input("Insira sua frase aqui: "))
formato=str(input("Ecolha o tipo de formato, (AA) para tudo maiusculo, (aa) para tudo minusculo, ou (Aa) para a primeira letra de cada palavra maiuscula: "))

if formato == "AA":
    print(frase.upper())
else:
    if formato == "aa":
        print(frase.lower())
    else:
        if formato == "Aa":
            print(frase.title())
        else:
            print("Tipo invalido")

#Podemos tambem usar o metodo de diminuir um pouco o codigo, como no exemplo abaixo

'''
if formato == "AA":
    print(frase.upper())
elif formato == "aa":
        print(frase.lower())
elif formato == "Aa":
            print(frase.title())
else:
    print("Tipo invalido")
'''

numero1= int(input("Informe um numero: "))
numero2= int(input("Informe um numero: "))
numero3= int(input("Informe um numero: "))
lista=(numero1,numero2,numero3)

print(lista)
#O len serve para dizer o tamanho das coisas, por exemplo, estamos usando ele abaixo para saber o comprimento da lista, que aqui sera de 3, pois temos 3 variaveis que iremos inserir na lista
print(len(lista))
print(max(lista))#retorna o valor maximo da lista, ou seja o numero maior
print(min(lista))#retorna o valor minimo da lista, ou seja o numero menor

soma= numero1+numero2+numero3

print(f"A soma entre {numero1}, {numero2} e {numero3} é igual á: {soma} ")

#outro modo mais facil de fazer essa soma seria sem usar uma variavel "soma", segue o exemplo
#o comando "sum" é usado para somar todos os dados inseridos na variavel lista
print(sum(lista))

#para colocar a lista em ordem crescente usamos o .sort, como no exemplo abaixo
lista.sort()
print(lista)

#e para escrever a lista em ordem descrescente usamos o .reverse, como no exemplo abaixo
lista.reverse()
print(lista)
