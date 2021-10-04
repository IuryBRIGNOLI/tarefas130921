Cnovos = ["Corolla","Compass","Onix","Civic","Kicks","Tiggo","Hilux"]
print(Cnovos)
Cusados = ["Corsa","Uno","Celta","Crossfox","Logan","Voyage","Fiesta"]
print(Cusados)

todos = [Cnovos+Cusados]
print(todos)

print("Carros em ordem alfábetica :",sorted(todos))

del todos[6]
print(todos)

del todos [13]
print(todos)


Cnovos.append(cit)
print(Cnovos)

Cnovos.append(duster)
print(Cnovos)

Cusados.append(clio)
print(Cusados)

Cnovos.append(gol)
print(Cusados)


if "Compass" in todos:
    print("Sim, está na lista!")
else:
    print("Não está na lista")

