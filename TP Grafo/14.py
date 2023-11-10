from grafo import Grafo


grafo = Grafo(dirigido= False)


grafo.insert_vertice('cocina')
grafo.insert_vertice('comedor')
grafo.insert_vertice('cochera')
grafo.insert_vertice('quincho')
grafo.insert_vertice('baño 1')
grafo.insert_vertice('baño 2')
grafo.insert_vertice('habitacion 1')
grafo.insert_vertice('habitacion 2')
grafo.insert_vertice('sala de estar')
grafo.insert_vertice('terraza')
grafo.insert_vertice('patio')

grafo.insert_arist('cocina', 'comedor', 6)
grafo.insert_arist('cocina', 'quincho', 4)
grafo.insert_arist('cocina', 'patio', 4)
grafo.insert_arist('quincho', 'baño 1', 4)
grafo.insert_arist('patio', 'baño 1', 5)
grafo.insert_arist('quincho', 'sala de estar', 8)
grafo.insert_arist('sala de estar', 'baño 2', 3)
grafo.insert_arist('sala de estar', 'habitacion 2', 3)
grafo.insert_arist('sala de estar', 'comedor', 6)
grafo.insert_arist('sala de estar', 'terraza', 9)
grafo.insert_arist('terraza', 'habitacion 1', 4)
grafo.insert_arist('terraza', 'habitacion 2', 6)
grafo.insert_arist('habitacion 1', 'comedor', 7)
grafo.insert_arist('baño 1', 'habitacion 2', 4)
grafo.insert_arist('baño 2', 'habitacion 1', 2)
grafo.insert_arist('cochera', 'baño 2', 8)
grafo.insert_arist('cochera', 'terraza', 4)
grafo.insert_arist('cochera', 'patio', 6)
grafo.insert_arist('terraza', 'patio', 9)





bosque = grafo.kruskal()

arbol = bosque[0].split(';')

metros_totales = 0

for nodo in arbol:

    metros_totales +=  int(nodo[-1:])


print(f"Se necesitan {metros_totales} metros para conectar todos los ambientes")
print()

ori = 'habitacion 1'
des = 'sala de estar'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if grafo.has_path(ori, des):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:

                if des == value[0]:
                    metros_cable = value[1]

                fin = value[2]

    
print(f"Se necesitan {metros_cable} metros de cable de red para conectar el router con el smart tv")