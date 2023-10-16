# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para 
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a 
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.




from arbol_binario import BinaryTree


lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

#b. listar los villanos ordenados alfabéticamente;
print('Villanos ordenados alfabeticamente:')
arbol.inorden_s_or_v(False)

print()
#c mostrar todos los superhéroes que empiezan con C;
print("Superheroes que empiezan con 'C':")
arbol.inorden_start_with('C')

#d determinar cuántos superhéroes hay el árbol;
print()
print(f"Hay {arbol.contar_heroes()} superheroes en el arbol")

print()
#e Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre

arbol.search_by_coincidence('do')

value = input('Ingrese el nombre que desea modificar: ')
pos = arbol.search(value)

if pos:
    tipo = pos.other_values
    arbol.delete_node(value)
    new_value = input('Ingrese nuevo nombre: ')
    arbol.insert_node(new_value, tipo)

else:
    print("No se encuentra")

print()

#f listar los superhéroes ordenados de manera descendente;
print(arbol.descendente())

#g

arbol_heroe = BinaryTree()
arbol_villano = BinaryTree()


arbol.bosque_heroe_villano(arbol_heroe, arbol_villano)

print("")
print("Heroes: ")
arbol_heroe.inorden()

print("")
print("Villanos: ")
arbol_villano.inorden()


