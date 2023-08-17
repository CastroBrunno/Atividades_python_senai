#codigo para saber se aluno foi reprovado ou aprovado

nota_portug=int(input("Informe a nota do aluno em portugues: "))
nota_matemat=int(input("Informe a nota do aluno em matematica: "))

if nota_portug >= 6 and nota_matemat >= 6:
    print("aluno aprovado")
elif nota_portug < 6 and nota_matemat < 6:
        print("Reprovado")
elif nota_portug >= 6 and nota_matemat < 6:
        print("Recuperação")
else:
        print("Recuperação")

#uma outra forme de fazer que o aluno nao podera tirar nota abaixo de 6 em nehuma materia se não sera reprovado seria usando o comando "or"
#Exemplo:
if nota_portug < 6 or nota_matemat < 5:
    print("Reprovado")
else:
    print("Aprovado")
#dessa maneira se o aluno tirar uma nota abaixo da media e a outra acima, ele estara aprovado de qualquer maneira, assim economizando linha no codigo


