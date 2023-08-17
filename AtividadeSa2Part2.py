# 2. Faça um programa que leia 4 valores, calcula a media e imprima positivo ou negativo (Para ser positivo a media deve ser acima de 1)

total= 0
contador= 0
while(contador < 4):
    nota=int(input("Insira a nota do aluno em sequencia: "))
    total=total+nota
    contador= contador + 1
media= total/4
print("A media das notas é: ")
print(media)

if media < 0:
    print("Nota negativa")
elif media > 1:
        print("Nota positiva")
elif media == 0:
            print("Nota nula")


# 3. Faça um programa que leia 20 valores inteiros e informe a media deles, o maior e o menor valor
menor=2000000000000000000000000
maior=0
Total= 0
Contador= 1
while(Contador < 11):
    valor=int(input(f"Insira o {Contador}º valor: "))
    Total=Total+valor
    Contador= Contador + 1 
    if valor > maior:
        maior= valor
    if valor < menor:
        menor= valor

print("O maior valor é: ")
print(maior)
print("O menor valor é: ")
print(menor)

Media= Total/10
print(Media)

# 4. Crie uma função para desenhar uma linha, usando o caractere '_' (underline). O tamanho da linha deve ser definido na chamada função
linha=int(input("Coloque a quantidade de linhas que deseja usar'____': "))
under="___"
print(under*linha)

# 5.

# 6.crie um programa que converta horas em segundos, conforme o valor que o usuario informar quando solicitadi a ele
horas=int(input("Escreva o valor de horas que deseja converter em segundos: "))
minutos=float(horas*60)
segundos= float(minutos*60)
print(f"{horas} horas convertidas em segundos são {segundos} segundos")

# 7.Altere o codigo a seguir para o menor numero de linhas possivel, mantendo o mesmo resultado

print("     *" , "    * *" , "   *   *", "  *     *", " ***   ***", "   *   *", "   *   *", "   *****", sep="\n")

