#Nesse codigo iremos fa\er o sistema de troco, porem, sem os comandos de repetições ou condições


from decimal import Decimal
compra = Decimal(input("Informe o valor da compra: "))
dinheiro = Decimal(input("Informe o valor pago: "))

troco = Decimal(dinheiro - compra)
print("O valor do troco é: R$", +troco)

lista = ["200", "100", "50", "20", "10", "5", "2", "1", "0.50", "0.25", "0.10", "0.05", "0.01"]

for valor in lista:
    calculo= int(troco / Decimal(valor))
    troco = troco - (calculo*Decimal(valor))
    if calculo > 0:
        print("Troco no valor de: R$" +valor, "quantidade é: ", +calculo )


#Dessa maneira abaixo, você precisara fazer uma variavel para cada nota, repetindo o codigo abaixo, mudando apenas o nome da variavel e o valor dela.
'''
cem = int(troco / Decimal("100"))
troco = troco - (cem*Decimal("100"))

print("Notas de R$ 100, quantidade: ", cem)
'''
