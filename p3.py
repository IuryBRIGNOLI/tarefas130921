contador = int(0)

um = input("Você telefonou para vitíma ? ")
if(um =="sim" or "Sim" or "SIM"):
     (contador+1)

dois = input("Esteve no local do crime ?")
if(dois == "Sim " or "sim " or "SIM"): 
    (contador+1)

tres = input("Mora perto da vítima ?")
if(tres == "sim " or "SIM " or "Sim"):
    (contador+1)

quatro = input("Devia para a vítima ?")
if(quatro == "sim" or "SIM" or "Sim" ):
     (contador+1)

cinco = input("Já trabalhou com a vítima ?")
if(cinco == "sim " or "Sim" or "SIM"):
   (contador+1)


if(contador>=2):
   print("Você é suspeita ")
if (contador>=3 and contador<=4):
    print("Você é cúmplice")
if (contador>=5):
    print("Você é o assassino")
if (contador<1):
    print("Você é inocente")     