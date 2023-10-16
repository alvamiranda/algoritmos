# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos 
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las 
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre

from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

nombre_tree = BinaryTree()
ranking_tree = BinaryTree()
especie_tree = BinaryTree()

read_lines.pop(0)

#a
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop()
    nombre_tree.insert_node(jedi[0], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
    especie_tree.insert_node(jedi[2], index+2)

#b
print()

print('Inorden por nombre:')
nombre_tree.inorden()

print()

print('Inorden por ranking:')
ranking_tree.inorden_file('jedis.txt')

print()

#c
print()

print('Barrido por nivel - Ranking')
ranking_tree.by_level()

print()

print('Barrido por nivel - Especie')
especie_tree.by_level()


print()
#d Mostrar info de Yoda y Luke Skywalker

print('#d')

pos = nombre_tree.search('yoda')

value= get_value_from_file('jedis.txt', pos.other_values)
print(f'Nombre: {value[0]} | Ranking: {value[1]} | Especie: {value[2]} | Master: {value[3]} | Color sable: {value[4]} | Año nacimiento: {value[6]}' )
print()

pos = nombre_tree.search('luke skywalker')

value= get_value_from_file('jedis.txt', pos.other_values)
print(f'Nombre: {value[0]} | Ranking: {value[1]} | Especie: {value[2]} | Master: {value[3]} | Color sable: {value[4]} | Año nacimiento: {value[6]}' )

print()


#e Mostrar todos los jedis con ranking 'Jedi Master'
print('#e Jedis con ranking jedi master: ')
ranking_tree.inorden_start_with_jedi('jedis.txt','jedi master')

print()

#f Jedis que utilizaron sable de luz color verde

print('#f Jedis que utilizaron sable de luz color verde: ')
nombre_tree.inorden_file_lightsaber('jedis.txt', 'green')

print()

#g Jedi cuyos maestros están en el archivo

print('Jedi cuyos maestros están en el archivo: ')
nombre_tree.inorder_master('jedis.txt')

print()

#h. mostrar todos los Jedi de especie “Togruta” o “Cerean”

print("Jedis de especie “Togruta” o “Cerean”:")

especie_tree.inorden_especie("jedis.txt")

print()

#i listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre
print("los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre")
nombre_tree.inorden_starts_with_a("a", "-")
