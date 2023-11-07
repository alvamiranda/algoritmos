from grafo import Grafo
from random import randint

grafo = Grafo(dirigido=False)

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leila", "Rey","Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8" ]

for personaje in personajes:
    grafo.insert_vertice(personaje)


aux=0
for personaje in personajes:
       
    for personaje2 in personajes[aux:]:

        if personaje != personaje2:
            grafo.insert_arist(personaje, personaje2, randint(0,10))

    aux = aux+1


# hallar el árbol de expansión minino y determinar si contiene a Yoda;

encontrar_yoda= False

bosque = grafo.kruskal()
for arbol in bosque:
    print('arbol expansion minimo')
    for nodo in arbol.split(';'):
        aux = nodo.find("Yoda")
        if aux != -1:
            encontrar_yoda= True
        print(nodo)

print()
if encontrar_yoda == True:
    print("Se contiene a yoda")
else: print("No se contiene a yoda")

