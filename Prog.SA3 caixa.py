#
from decimal import Decimal
print("="*30) 
#valor para leitura 86,45 e 100
totalcompras= (Decimal(input("Valor total das compras R$"))) 
valorpg=  (Decimal(input("Valor recebido R$")))
troco =(Decimal) (valorpg - totalcompras)
print("Seu troco é R$", troco)
cedula =200
totalced = 0
while float:
    if troco >= cedula:
        troco -=Decimal (cedula)
        totalced +=1 
    else:
        if totalced > 0:
            print("Total de",totalced, "cédula de R$",cedula)
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula ==20:
            cedula = 10
        elif cedula ==10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula ==2:
            cedula = 1
        elif cedula == 1:
            cedula = 0.50
        elif cedula ==0.50:
            cedula = 0.25
        elif cedula == 0.25:
            cedula = 0.10
        elif cedula == 0.10:
            cedula = 0.5
        elif cedula ==0.5:
            cedula = 0.1
        totalced = 0
        if troco == 0:
            break

print("="*30)








