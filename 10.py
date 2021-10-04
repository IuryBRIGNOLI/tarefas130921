x = int(input("Digite um número"))
y = int(input("Digite outro número"))

z = input("Escolha\n 1- +\n2- -\n3- x\n4- /(dividir)")

if(z == "1"):
    print(x+y,"Resultado")
elif(z == "2"):
    print(x-y,"Resultado")
elif(z=="3"):
    print(x*y,"Resultado")
elif(z=="4"):
    print(x/y,"Resultado")
else:
    print("Por favor revejava sua escolhas")    