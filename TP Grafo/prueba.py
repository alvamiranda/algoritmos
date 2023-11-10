from grafo import Grafo
from random import randint

grafo = Grafo(dirigido=False)

planetas = [
    "Alderaan",
    "Endor",
    "Dagobah",
    "Hoth",
    "Tatooine",
    "Kamino",
    "Naboo",
    "Mustafar",
    "Scarif",
    "Bespin",
    "Coruscant",
    "Geonosis",
    "Kashyyyk",
    "Mandalore",
    "Jakku",
    "Exegol",
    "Sullust"
]


for planeta in planetas:
    grafo.insert_vertice(planeta)

aux=0
for planeta in planetas:
       
    for planeta2 in planetas[aux:]:

        if planeta != planeta2:
            grafo.insert_arist(planeta, planeta2, randint(1000,10000))

    aux = aux+1

# repetidos2 = []
# for planeta in planetas:
#     repetidos = []
    
#     for i in range(4):

#         planeta_des = planetas[randint(0, 16)]
    
#         if (planeta_des != planeta and (planeta_des not in repetidos) and (planeta_des not in repetidos2)):
#             grafo.insert_arist(planeta, planeta_des, randint(1000,10000))
#             repetidos.append(planeta_des)

     

#     repetidos2.append(planeta)
    

grafo.barrido()


bosque = grafo.kruskal()

print('arbol expansion minima')
arbol = bosque[0].split(';')

for nodo in arbol:
    print(nodo)

print()
print("camino mas corto desde tatooine hasta dagobah")
ori = 'Tatooine'
des = 'Dagobah'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des)):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0])
                fin = value[2]



print()



print('Paises a los que puede llegar Tatooine')

pos= grafo.search_vertice('Endor')


grafo.amplitude_list(pos)