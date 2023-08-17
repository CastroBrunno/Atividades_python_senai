from decimal import Decimal
from decimal import Decimal
from threading import BrokenBarrierError 


valor_pagp = Decimal(input("Valor pago pelo cliente: "))
valor_produto = Decimal(input("Valor do produto: "))
troco = valor_pagp - valor_produto
print("o valor do troco é: ", troco)
nota = 200
troconota = 0

while True:
    if troco >= nota:
        troco = troco - nota
        troconota = troconota + 1
    else:
        print(f"O troco é de {troconota} nota/moeda de R${nota}.")

        if nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            nota = 1
        elif nota == 1:
            nota = Decimal("0.50")
        elif nota == Decimal("0.50"):
            nota = Decimal("0.25")
        elif nota == Decimal("0.25"):
            nota = Decimal("0.10")
        elif nota == Decimal("0.10"):
            nota = Decimal("0.05")
        elif nota == Decimal("0.05"):
            nota = Decimal("0.01")
        troconota = 0 
        if troco == 0:
            break
        
