from arbol_binario import BinaryTree

arbol = BinaryTree()

data = [
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tifon', 'derrotado': "Zeus"},
    {'name': 'Equidna', 'derrotado': "Argos Panoptes"},
    {'name': 'Dino', 'derrotado': None},
    {'name': 'Pefedo', 'derrotado': None},
    {'name': 'Enio', 'derrotado': None},
    {'name': 'Caribdis', 'derrotado': None},
    {'name': 'Euriale', 'derrotado': None},
    {'name': 'Esteno', 'derrotado': None},
    {'name': 'Medusa', 'derrotado': "Perseo"},
    {'name': 'Ladon', 'derrotado': "Heracles"},
    {'name': 'Aguila del Caucaso', 'derrotado': None},
    {'name': 'Talos', 'derrotado': "Medea"},
    {'name': 'Cerbero', 'derrotado': None},
    {'name': 'Toro de Creta', 'derrotado': "Teseo"},
    {'name': 'Cierva Cerinea', 'derrotado': None},
    {'name': 'Jabali de Erimanto', 'derrotado': None},
    {'name': 'Basilisco', 'derrotado': None},
    {'name': 'Sirenas', 'derrotado': None},
    {'name': 'Aves del Estinfalo', 'derrotado': None},
]

for criatura in data:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado'], 'capturada': None, 'descripcion': None})

#a listado inorden de las criaturas y quienes la derrotaron

print("listado inorden de las criaturas y quienes la derrotaron")

arbol.inorden_add_field()



print()

#b se debe permitir cargar una breve descripción sobre cada criatura

arbol.cargar_descripcion()

print()

#c  mostrar toda la información de la criatura Talos;
pos = arbol.search('Talos')

print("mostrar toda la información de la criatura Talos")

print(f"{pos.value} - {pos.other_values}")

print()

#d determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas

ranking = {}

arbol.inorden_ranking(ranking)

print("dioses que derrotaron mayor cantidad de criaturas")
print(ranking)

print()

#f listar las criaturas derrotadas por Heracles

print("criaturas derrotadas por Heracles")
arbol.inorden_derrotado_por('Heracles')

print()

#g cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo

#h modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó

print("#H")

criaturas_atrapadas_heracles = {"Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabali de Erimanto"}

for criatura in criaturas_atrapadas_heracles:
    pos = arbol.search(criatura)
    pos.other_values["capturada"] = "Heracles"
    print(f"{pos.value} - {pos.other_values}")

print()

#i se debe permitir búsquedas por coincidencia

print("Busqueda por coincidencia")

arbol.search_by_coincidence("S")

print()

#j  eliminar al Basilisco y a las Sirenas

print("#j")

arbol.delete_node('Sirenas')
arbol.delete_node('Basilisco')

print()
#k modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias

pos = arbol.search("Aves del Estinfalo")
pos.other_values['derrotado'] = 'Heracles'

#l  modifique el nombre de la criatura Ladón por Dragón Ladón

pos = arbol.search("Ladon")

new_value = "Dragon Ladon"
other_values = pos.other_values

arbol.delete_node("Ladon")
arbol.insert_node(new_value, other_values)

print()

#m realizar un listado por nivel del árbol

print("Listado por nivel: ")
arbol.by_level()

print()

#n muestre las criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles")

arbol.inorden_capturado_por("Heracles")