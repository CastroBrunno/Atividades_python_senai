preco=float(input("Informe o valor total da compra: "))
valor_recebido=float(input("Informe o valor recebido: "))
troco= valor_recebido - preco
print("o troco será R$: %.2f"%troco)

nota200=0
nota100=0
nota50=0
nota20=0
nota10=0
nota5=0
nota2=0
nota1=0
moeda50=0
moeda25= 0
moeda10 = 0
moeda5= 0
moeda01= 0

while (troco >= 200):
    troco= troco- 200
    nota200= nota200 + 1
else:
    while (troco >= 100):
        troco= troco- 100
        nota100= nota100 + 1
    else:
        while (troco >= 50):
             troco= troco- 50
             nota50= nota50 + 1
        else:
            while (troco >= 20):
                troco= troco- 20
                nota20= nota20 + 1
            else:
                while (troco >= 10):
                    troco= troco - 10
                    nota10= nota10 + 1
                else:
                    while (troco >= 5):
                        troco= troco - 5
                        nota5= nota5 + 1
                    else:
                        while (troco >= 2):
                            troco= troco - 2
                            nota2= nota2 + 1
                        else:
                            while (troco >= 1):
                                troco= troco - 1
                                nota1=nota1 + 1
                            else:
                                while troco >= 0.50:
                                    troco= troco - 0.50
                                    moeda50= moeda50 + 1
                                else:
                                    while troco >= 0.25:
                                        troco= troco - 0.25
                                        moeda25= moeda25 + 1
                                    else:
                                        while troco >= 0.10:
                                            troco= troco - 0.10
                                            moeda10= moeda10 + 1
                                        else:
                                            while troco >= 0.05:
                                                troco= troco - 0.05
                                                moeda5= moeda5 +1
                                            else:
                                                while troco >= 0.01:
                                                    troco= troco - 0.01
                                                    moeda01= moeda01 +1

print(f"Tens que dar {nota200} notas de 200 Reais de troco")
print(f"Tens que dar {nota100} notas de 100 Reais de troco")
print(f"Tens que dar {nota50} notas de 50 Reais de troco")
print(f"Tens que dar {nota20} notas de 20 Reais de troco")
print(f"Tens que dar {nota10} notas de 10 Reais de troco")
print(f"Tens que dar {nota5} notas de 5 Reais de troco")
print(f"Tens que dar {nota2} notas de 2 Reais de troco")
print(f"Tens que dar {nota1} notas de 1 Real de troco")
print(f"Tens que dar {moeda50} moeda de 50 Centavos de troco")
print(f"Tens que dar {moeda25} moeda de 25 Centavos de troco")
print(f"Tens que dar {moeda10} moeda de 10 Centavos de troco")
print(f"Tens que dar {moeda5} moeda de 5 Centavos de troco")
print(f"Tens que dar {moeda01} moeda de 1 Centavo de troco")



#Modo que o professor fez. Abaixo
 






