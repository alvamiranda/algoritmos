from grafo import Grafo
from random import randint

grafo = Grafo(dirigido= False)

dic_maravillas= [
    {'nombre': 'gran muralla china', 'tipo': 'arquitectonica', 'pais': 'china'},
    {'nombre': 'petra', 'tipo': 'arquitectonica', 'pais': 'jordania'},
    {'nombre': 'cristo redentor', 'tipo': 'arquitectonica', 'pais': 'brasil'},
    {'nombre': 'machu picchu', 'tipo': 'arquitectonica', 'pais': 'peru'},
    {'nombre': 'coliseo', 'tipo': 'arquitectonica', 'pais': 'italia'},
    {'nombre': 'estatua de la libertad', 'tipo': 'arquitectonica', 'pais': 'estados unidos'},
    {'nombre': 'taj mahal', 'tipo': 'arquitectonica', 'pais': 'india'},

    {'nombre': 'gran barrera de coral', 'tipo': 'natural', 'pais': 'australia'},
    {'nombre': 'gran cañón', 'tipo': 'natural', 'pais': 'estados unidos'},
    {'nombre': 'amazonia', 'tipo': 'natural', 'pais': 'brasil'},
    {'nombre': 'cataratas del iguazu', 'tipo': 'natural', 'pais': 'brasil'},
    {'nombre': 'bahia de ha long', 'tipo': 'natural', 'pais': 'vietnam'},
    {'nombre': 'isla de jeju', 'tipo': 'natural', 'pais': 'corea del sur'},
    {'nombre': 'parque nacional de komodo', 'tipo': 'natural', 'pais': 'indonesia'}

]

#carga

class Maravilla:

    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.tipo= tipo
        self.pais = pais

    def __str__(self):
        return f"{self.nombre} - {self.pais} - {self.tipo}"

for maravilla in dic_maravillas:
    grafo.insert_vertice(Maravilla(maravilla['nombre'], maravilla['pais'], maravilla['tipo']), criterio ='nombre')



#carga tipo arquitectonicas
aux = 0
for maravilla in dic_maravillas[:6]:
    

    for maravilla2 in dic_maravillas[aux + 1:7]:
        grafo.insert_arist(maravilla['nombre'], maravilla2['nombre'], randint(1000,10000), criterio_vertice='nombre')

        
    aux = aux +1

#carga tipo naturales
aux = 0
for maravilla in dic_maravillas[7:-1]:
    

    for maravilla2 in dic_maravillas[aux + 8:]:
        grafo.insert_arist(maravilla['nombre'], maravilla2['nombre'], randint(1000,10000), criterio_vertice='nombre')
        
    aux = aux +1

#arbol de expansion minimo de cada tipo
bosque = grafo.kruskal()
for arbol in bosque:
    print()
    print('Arbol')
    for nodo in arbol.split(';'):
        print(nodo)

print()
#determinar si existen paises qee dispongan de maravillas naturales y arquitectonicas
paises_con_arq_y_nat=[]

for pos in range(grafo.size()):
    value = grafo.get_element_by_index(pos)

    for pos_2 in range(grafo.size()):
        value_2 = grafo.get_element_by_index(pos_2)
        if (value[0].tipo != value_2[0].tipo) and (value[0].pais == value_2[0].pais) and (value[0].pais not in paises_con_arq_y_nat):
            paises_con_arq_y_nat.append(value_2[0].pais)

if len(paises_con_arq_y_nat) != 0:
    print(f"Existen paises con maravillas naturales y arquitectonicas: {paises_con_arq_y_nat}")
else: print("No existen paises con maravillas naturales y arquitectonicas")

print()

paises_con_mismo_tipo = []
for pos in range(grafo.size()):
    value = grafo.get_element_by_index(pos)

    for pos_2 in range(grafo.size()):
        value_2 = grafo.get_element_by_index(pos_2)
        if (value[0].tipo == value_2[0].tipo) and (value[0].pais == value_2[0].pais) and (value[0].nombre != value_2[0].nombre) and (value[0].pais not in paises_con_mismo_tipo):
           paises_con_mismo_tipo.append(value_2[0].pais)

if len(paises_con_mismo_tipo) != 0:
    print(f"Existen paises con mas de una maravilla del mismo tipo: {paises_con_mismo_tipo}")
else: print("No existen paises con mas de una maravilla del mismo tipo")