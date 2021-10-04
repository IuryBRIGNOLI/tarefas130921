hora = float(input("Qual é o valor da sua hora ? "))

htb = float(input("Quantas horas trabalhasse ?  "))

sb = float(hora*htb)
print("Seu salário bruto é ", sb)

impp =  float(sb-0.11)
desimp = float(sb-impp)
print("Valor pago ao imposto de renda é {:.2f}".format(impp))
print("O desconto aplicado foi de  {:.2f}".format(desimp))

inss = float (sb-0.08)
desinss = float(sb - inss)
print("Valor pago ao inss é {:.2f}".format(inss))
print("O desconto aplicado foi de  {:.2f}".format(desinss))

sind = float (sb-0.05)
dessind = float(sb - sind)
print("Valor pago ao inss é {:.2f}".format(sind))
print("O desconto aplicado foi de  {:.2f}".format(dessind))

print("Sálario bruto : {:.2f}".format(sb))
print("Desconto do imposto de renda : {:.2f}".format(desimp))
print("Desconto do inss :{:.2f} ".format(desinss))
print("Desconto do sindicado {:.2f} ".format(dessind))

salario = float(sb - 0.11 - 0.08 - 0.05 )
print("Seu salário com desconto aplicados : {}".format(salario))






